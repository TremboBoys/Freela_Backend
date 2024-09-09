from core.perfil.models import CategoriaFreelancer
from core.perfil.serializer import CategoriaFreelancerSerializer
from rest_framework.viewsets import ModelViewSet

class CategoriaFreelancerViewSet(ModelViewSet):
    queryset = CategoriaFreelancer.objects.all()
    serializer_class = CategoriaFreelancerSerializer