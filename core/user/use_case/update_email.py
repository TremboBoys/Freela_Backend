from core.user.models import User
from rest_framework.response import Response
from rest_framework import status

def update_email(old_email, new_email):
    try:
        user = User.objects.get(email=old_email)
        user.email = new_email
        user.save()
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Update email!"}, status=status.HTTP_200_OK)