from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.user.models import User
from core.user.permissions import admin_group, freelancer_group, contratante 
from rest_framework_simplejwt.tokens import RefreshToken

 
def authenticate_user(email):
    try:
        user = User.objects.get(email=email)
        if user.type_user == 1:
            user.groups.add(admin_group)
        elif user.type_user == 2:
            user.groups.add(contratante)
        else: 
            user.groups.add(freelancer_group)
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token), 
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
