from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer
from core.perfil.models import Perfil, Hability, Nacionality, Area, SubArea, MyProjects, MyCompetency, Pro, ChoiceProject

class PerfilSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        fields = "__all__"

class HabilitySerializer(ModelSerializer):
    class Meta:
        model = Hability
        fields = "__all__"

class NacionalitySerializer(ModelSerializer):
    class Meta:
        model = Nacionality
        fields = "__all__"

class AreaSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"

class SubAreaSerializer(ModelSerializer):
    class Meta:
        model = SubArea
        fields = "__all__"

class MyProjectSerializer(ModelSerializer):
    class Meta:
        model = MyProjects
        fields = "__all__"

class MyCompetencySerializer(ModelSerializer):
    class Meta:
        model = MyCompetency
        fields = "__all__"


class ProSerializer(ModelSerializer):
    class Meta:
        model = Pro
        fields = "__all__"

class ChoiceProjectSerializer(ModelSerializer):
    class Meta:
        model = ChoiceProject
        fields = "__all__"