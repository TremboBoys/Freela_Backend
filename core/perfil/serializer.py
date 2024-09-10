from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer
from core.perfil.models import Perfil

class PerfilSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        fields = "__all__"