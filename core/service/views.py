from rest_framework.viewsets import ModelViewSet
from core.service.models import Service, ContractService
from core.service.serializer import ServiveSerializer, ContractServiceSerializer
from utils.viewset.service_view import ContractServiceModelViewSet

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiveSerializer
class ContractServiceViewSet(ContractServiceModelViewSet):
    queryset = ContractService.objects.all()
    serializer_class = ContractServiceSerializer
