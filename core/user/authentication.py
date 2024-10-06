from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.user.models import User
from core.user.permissions import admin_group, freelancer_group, contratante 
from rest_framework_simplejwt.tokens import RefreshToken

 
def authenticate_user(email):
    try:
        user = User.objects.get(email=email)    
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

        if not email:
            return Response({"message": "email are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        resp = authenticate_user(email=email)
                
        if resp == None:
            return Response({"message": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(resp, status=status.HTTP_200_OK)


    
