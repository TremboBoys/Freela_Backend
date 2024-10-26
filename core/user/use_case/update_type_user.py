from rest_framework.response import Response
from rest_framework import status
from core.user.models import User

def updateTypeUser(email, type_user):

    try:
        user = User.objects.get(email=email)
        if type_user == 'contractor':
            numberType = 2
        else:
            numberType = 3
        user.type_user = numberType
        user.save()
    except User.DoesNotExist as error:
        return Response({"message": "User not found!"}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({"message": "Updated password"}, status=status.HTTP_200_OK)