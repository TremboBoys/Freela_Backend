from rest_framework.viewsets import ModelViewSet
from core.user.serializer import UserSerializer
from core.user.models import User

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


