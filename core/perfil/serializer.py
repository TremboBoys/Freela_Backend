from rest_framework.serializers import ModelSerializer
from core.perfil.models import CategoriaFreelancer, MyProject, Hability, MyHability, Perfil

class CategoriaFreelancerSerializer(ModelSerializer):
    class Meta:
        model = CategoriaFreelancer
        fields = '__all__'

class MyProjectSerializer(ModelSerializer):
    class Meta:
        model = MyProject
        fields = '__all__'

class HabilitySerializer(ModelSerializer):
    class Meta:
        model = Hability
        fields = '__all__'

class MyHabilitySerializer(ModelSerializer):
    class Meta:
        model = MyHability
        fields = '__all__'

class PerfilSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'
