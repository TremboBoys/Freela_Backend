from rest_framework.viewsets import ModelViewSet
from core.service.models import Service
from core.service.serializer import ServiveSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiveSerializer