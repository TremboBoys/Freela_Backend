from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from core.perfil.models import Perfil, Hability, Nacionality, Area, SubArea, MyProjects, MyCompetency, Pro, ChoiceProject, PerfilAvaliation
from core.user.models import User
from uploader.serializers.image import ImageSerializer
from core.project.models import Project
from core.proposal.models import AcceptProposal
from cloudinary.utils import cloudinary_url



class UserNestedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'username', 'email']
        
class PerfilSerializer(ModelSerializer):
    user = UserNestedSerializer()
    projects_in_execution = SerializerMethodField()
    url_image = SerializerMethodField()
    
    class Meta:
        model = Perfil
        fields = ['balance', 'is_public', 'user', 'price_per_hour', 'nacionality', 'payment_type', 'about_me', 'area', 'sub_area', 'number_projects_in_execution', 'is_pro', 'access_token_mercado_pago', 'refresh_token_mercado_pago', 'expiration_date_access_token_mercado_pago', 'expiration_date_refresh_token_mercado_pago', 'collector_id_mercado_pago', 'avaliation', 'every_avaliations', 'image_perfil', 'projects_in_execution', 'url_image']
        depth = 1    
    
    def get_projects_in_execution(self, obj):
        print(obj)
        projects = AcceptProposal.objects.filter(proposal__perfil=obj, proposal__project__in_execution=True)
        return len(projects)
        
    def get_url_image(self, obj):
        if obj.image_perfil and obj.image_perfil.public_id:
            url, _ = cloudinary_url(obj.image_perfil.public_id)
            return url
        return None
class PerfilCurrentUserSerializer(ModelSerializer):
    projects_in_execution = SerializerMethodField()
    url_image = SerializerMethodField()
    class Meta:
        model = Perfil
        fields = "__all__"
        depth = 2
        
    def get_projects_in_execution(self, obj):
        projects = AcceptProposal.objects.filter(proposal__perfil=obj, proposal__project__in_execution=True)
        return len(projects)
    
    def get_url_image(self, obj):
        if obj.image_perfil and obj.image_perfil.public_id:
            url, _ = cloudinary_url(obj.image_perfil.public_id)
            return url
        return None
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
# class PerfilSerializer(ModelSerializer):
#     projects_in_execution = SerializerMethodField()
#     url_image = SerializerMethodField()
#     class Meta:
#         model = Perfil
#         fields = "__all__"
#         depth = 1
        
#     def get_projects_in_execution(self, obj):
#         print(obj)
#         projects = AcceptProposal.objects.filter(proposal__perfil=obj, proposal__project__in_execution=True)
#         return len(projects)
        
#     def get_url_image(self, obj):
#         if obj.image_perfil and obj.image_perfil.public_id:
#             url, _ = cloudinary_url(obj.image_perfil.public_id)
#             return url
#         return None
        
class PerfilAvaliationSerializer(ModelSerializer):
    class Meta:
        model = PerfilAvaliation
        fields = "__all__"