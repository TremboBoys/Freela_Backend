from core.service.models import ContractService
from core.service.serializer import ContractServiceSerializer
from utils.viewset.service_view import ContractServiceModelViewSet
from rest_framework.viewsets import ModelViewSet
class ContractServiceViewSet(ContractServiceModelViewSet):
    queryset = ContractService.objects.all()
    serializer_class = ContractServiceSerializer