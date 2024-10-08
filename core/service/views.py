from core.service.models import ContractService
from core.service.serializer import ContractServiceSerializer
from utils.viewset.service_view import ContractServiceModelViewSet
class ContractServiceViewSet(ContractServiceModelViewSet):
    queryset = ContractService.objects.all()
    serializer_class = ContractServiceSerializer