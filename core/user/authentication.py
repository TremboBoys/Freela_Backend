from passageidentity import Passage
from config import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.user.models import User


def authenticate_user(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist as error:
        return None

    print("User logged")

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({"message": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        if authenticate_user(email=email):
            return Response({"message": "Logged"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Not allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
