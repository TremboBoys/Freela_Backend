from rest_framework import mixins
from utils.mixins.create_contract_service import CreateContractServiceMixim
from utils.mixins.list_contract import ListContractModelMixin
from rest_framework.viewsets import GenericViewSet

class ContractServiceModelViewSet(
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     ListContractModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    pass