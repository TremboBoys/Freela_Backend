from rest_framework.response import Response
from rest_framework import status
from core.user.models import User
from django.contrib.auth.hashers import make_password

def updatePassword(email, password):

    try:
        user = User.objects.get(email=email)
        user.password = make_password(password=password)
        user.save()
    except User.DoesNotExist as error:
        return Response({"message": "User not found!"}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({"message": "Updated password"}, status=status.HTTP_200_OK)