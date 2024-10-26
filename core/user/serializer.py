from rest_framework.serializers import ModelSerializer
from core.user.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password', 'type_user']  

        extra_kwargs = {
            'code': {'write_only': True},
        }
        
    