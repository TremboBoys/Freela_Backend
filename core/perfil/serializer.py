from rest_framework.serializers import ModelSerializer
from core.perfil.models import CategoriaFreelancer


class CategoriaFreelancerSerializer(ModelSerializer):
    class Meta:
        model = CategoriaFreelancer
        fields = "__all__"
