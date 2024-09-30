from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from core.user.models import EmailVerification
from core.user.models import User
from django.contrib.auth.hashers import make_password
from core.user.serializer import UserSerializer
from django.shortcuts import get_object_or_404
class SendVericationCodeAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({"message": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        code = random.randint(100000, 999999) 
        try:
            possible_user = EmailVerification.objects.create(email=email, code=code)
            possible_user.save()
        except Exception as error:
            return Response({"message": f"Erro in api for email verification, {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"message": "Code invite!"}, status=status.HTTP_201_CREATED)

class UserAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        username = request.data.get('username')
        password = request.data.get('password')
        code = request.data.get('code') 

        if not name or not username or not password or not code:
            return Response({"message": "Dates required don't offers"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = EmailVerification.objects.get(code=code)
            email = token.email
        except EmailVerification.DoesNotExist as error:
            return Response({"message": "Code doesn't exists"}, status=status.HTTP_404_NOT_FOUND)

        try:
            hashed_password = make_password(password=password)
            user = User.objects.create(username=username, name=name, email=email, password=hashed_password)
            user.save()
            token.delete()
        except Exception as error:
            return Response({"messsage": f"{error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"messaga": "User created"}, status=status.HTTP_200_OK)
    
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
        pk = request.data.get('id')
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "User deleted"}, status=status.HTTP_200_OK)
    
    def put(self, request):
        user_id = request.data.get('id')
        user = get_object_or_404(User, pk=user_id)

        action = request.data.get('action')

        

        if action == "update_email":
            new_email = request.data.get('new_email')

            if not new_email:
                return Response({"message": "email for update is required"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                email_user = User.objects.get(id=user_id)
                email_user.email = new_email
                email_user.save()
            except User.DoesNotExist as error:
                return Response({"message": "User not found!"}, status=status.HTTP_404_NOT_FOUND)




    
        