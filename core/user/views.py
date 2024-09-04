from rest_framework.viewsets import ModelViewSet
from core.user.models import User
from core.user.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "Email foi enviado com sucesso!"}, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def confirm_email(self, request):
        email = request.data.get('email')
        token = request.data.get('token')
        try:
            user = User.objects.get(email=email)
            if user.confirmation_token == token:
                user.is_active = True
                user.confirmation_token = None
                user.save()
                return Response({"message": "Email confirmado com sucesso!"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Error!": "Token inválido!"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "User not found!"}, status=status.HTTP_404_NOT_FOUND)
        