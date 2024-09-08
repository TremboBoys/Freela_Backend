from rest_framework.serializers import ModelSerializer
from core.user.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'confirmation_token': {'write_only': True},
            'is_active': {'read_only': True}
        }
        
    