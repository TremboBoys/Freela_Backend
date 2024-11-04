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
from passage import Passage
from core.user.permissions import freelancer_group, contratante

passage = Passage(api_key=settings.PASSAGE_APP_KEY)
class UserAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        type_user = request.data.get('type_user')
        
        if name or username or email or password or type_user == None or len(password) < 8:
            return Response({"message": "Has a incomplete data"}, status=status.HTTP_400_BAD_REQUEST)

        
        if User.objects.get(email=email):
            return Response({"message": "User already exists"}, status=status.HTT_409_CONFLICT)
        
        try:
            if type_user == "contractor":
                type_user = 2
            elif type_user == "freelancer":
                type_user = 3
            user = User.objects.create(name=name, username=username, password=make_password(password=password), type_user=type_user, email=email)
            if user.type_user == 2:
                user.groups.add(contratante)
            else:
                user.groups.add(freelancer_group)
            user.save()
        except Exception as error:
            return Response({"message": error}, status=status.HTTP_404_NOT_FOUND)
        
        response = passage.create_user(email=email, password=password)

        if response.status_code == 200:
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Error in create user"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
                
                

        

    
        