from rest_framework.viewsets import ModelViewSet 
from core.perfil.models import CategoriaFreelancer, MyProject, Hability, MyHability, Perfil
from core.perfil.serializer import CategoriaFreelancerSerializer, MyProjectSerializer, HabilitySerializer, MyHabilitySerializer, PerfilSerializer

class CategoriaFreelancerViewSet(ModelViewSet):
    queryset = CategoriaFreelancer.objects.all()
    serializer_class = CategoriaFreelancerSerializer

class MyProjectViewSet(ModelViewSet):
    queryset = MyProject.objects.all()
    serializer_class = MyProjectSerializer

class HabilityViewSet(ModelViewSet):
    queryset = Hability.objects.all()
    serializer_class = HabilitySerializer

class MyHabilityViewSet( ModelViewSet):
    queryset = MyHability.objects.all()
    serializer_class = MyHabilitySerializer

class PerfilViewSet(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
