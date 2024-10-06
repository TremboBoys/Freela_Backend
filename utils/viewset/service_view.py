from rest_framework import mixins
from utils.mixins.create_contract_service import CreateContractServiceMixim
from rest_framework.viewsets import GenericViewSet

class ServiceViewSet(CreateContractServiceMixim,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    pass