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

        
