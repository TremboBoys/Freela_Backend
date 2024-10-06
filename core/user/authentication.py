from passageidentity import Passage
from config import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.user.models import User
from core.user.permissions import admin_group, freelancer_group, contratante 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

 
def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)    
        print("K")
        print(check_password(password, user.password))
        if not check_password(password, user.password):  # Fix this line
            return None
        print("J")
        
        try:
            if user.type_user == 'admin':
                print("A")
                admin_group.user_set.add(user)  # Adicione a instância do usuário
            elif user.type_user == "contratante":
                print("c")
                contratante.user_set.add(user)  # Adicione a instância do usuário
            else:      
                try:
                    freelancer_group.user_set.add(user)  # Adicione a instância do usuário
                except Exception as error:
                    print(error)
        except Exception as error:
            return None

    
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        refresh_token = str(refresh)

        return {
            'access_token': access,
            'refresh': refresh_token
        }
            
    except User.DoesNotExist as error:
        return None


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"message": "password and email are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        resp = authenticate_user(email=email, password=password)
                
        if resp == None:
            return Response({"message": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(resp, status=status.HTTP_200_OK)


    
