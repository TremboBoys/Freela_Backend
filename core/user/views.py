from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from core.user.models import EmailVerification
from core.user.models import User
from django.contrib.auth.hashers import make_password
from core.user.serializer import UserSerializer
from django.shortcuts import get_object_or_404
from core.user.use_case.update_email import update_email
from core.user.use_case.update_password import updatePassword
from core.user.use_case.update_type_user import updateTypeUser
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
        type_user = request.data.get('type_user')

        if not name or not username or not password or not code or not type_user:
            return Response({"message": "Dates required don't offers"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = EmailVerification.objects.get(code=code)
            email = token.email
        except EmailVerification.DoesNotExist as error:
            return Response({"message": "Code doesn't exists"}, status=status.HTTP_404_NOT_FOUND)

        try:
            hashed_password = make_password(password=password)
            user = User.objects.create(username=username, name=name, email=email, password=hashed_password, type_user=type_user)
            user.save()
            token.delete()
        except Exception as error:
            return Response({"messsage": f"{error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"message": "User created"}, status=status.HTTP_201_CREATED )
    
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
        pk = request.data.get('id')
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "User deleted"}, status=status.HTTP_200_OK)
    
    def patch(self, request):
        action = request.data.get('action')
        code = request.data.get('code')
       
        if not action or not code:
           return Response({"message": "Code and action is required"})
        try:
            userUpdated = EmailVerification.objects.get(code=code)
            old_email = userUpdated.email
            userUpdated.delete()
        except EmailVerification.DoesNotExist as error:
           return Response({"message": "Token not found"}, status=status.HTTP_404_NOT_FOUND)
       
        if action == "update_email":
           newEmail = request.data.get('email')
           return update_email(old_email=old_email, new_email=newEmail)

        elif action == "update_password":
            password = request.data.get('password')
            return updatePassword(email=old_email, password=password)
        elif action == "update_type_user":
            newType = request.data.get('type_user')
            if newType == 'admin':
                return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
            else: 
                updateTypeUser(old_email, newType)
                return Response({"message": "Type user updated!"}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


            
           





    
        