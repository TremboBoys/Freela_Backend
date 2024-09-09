from rest_framework.views import APIView
from core.user.models import User
from rest_framework.response import Response
from rest_framework import status
from core.user.models import EmailVerification
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError

class UserAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        name = request.data.get('name')
        password = request.data.get('password')
        code = request.data.get('code')

        if not email or not password:
            return Response({'message': "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        email_verification = EmailVerification.objects.filter(email=email, code=code).first()

        if email_verification:
            if User.objects.filter(email=email).exists():
                return Response({'message': "Email is already registered"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                hashed_password = make_password(password)
                new_user = User.objects.create(email=email, username=username, name=name, password=hashed_password)
                new_user.save()
                email_verification.delete() 
                return Response({"message": "User created!"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"message": "A user with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message": "Invalid verification code or email"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        code = request.data.get('token')

        if not email or not password or not code:
            return Response({"message": "Email, password, and token are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        email_verification = EmailVerification.objects.filter(email=email, code=code).first()
        if not email_verification:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user.password = make_password(password=password)
            user.save()
            email_verification.delete()
            return Response({"message": "Password updated"}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request):
        data = request.data
        code = data['code']
        email = data['email']
        email_for_update = data['email_update']
        if not email or not code:
            return Response({"message": "Code or email are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        email_verification = EmailVerification.objects.filter(code=code, email=email).first()

        if not email_verification:
            return Response({"message": "User not found in email_verification"}, status=status.HTTP_404_NOT_FOUND)

        try:
            user.email = email_for_update
            user.save()
            email_verification.delete()
            return Response({"message": "Email update!"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({"message": f"Internal server error: {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            