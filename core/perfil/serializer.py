from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.perfil.models import Perfil, Hability, Nacionality, Area, SubArea, MyProjects, MyCompetency, Pro, ChoiceProject
from core.user.models import User
from uploader.serializers.image import ImageSerializer

class UserNestedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'username', 'email']

class PerfilSerializer(ModelSerializer):
    user = UserNestedSerializer()
    class Meta:
        model = Perfil
        fields = ['balance', 'is_public', 'user', 'price_per_hour', 'nacionality', 'photo', 'payment_type', 'about_me', 'area', 'sub_area']
        depth = 1
        

class PerfilCurrentUserSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        fields = "__all__"
        depth = 1
        
        

class NacionalitySerializer(ModelSerializer):
    class Meta:
        model = Nacionality
        fields = "__all__"
        depth = 1

class HabilitySerializer(ModelSerializer):
    class Meta:
        model = Hability
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
        
class PerfilSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        fields = "__all__"