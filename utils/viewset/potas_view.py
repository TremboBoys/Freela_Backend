from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from utils.mixins.potas_mixin import SpeciafilyListModelMixin

class PotasViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   SpeciafilyListModelMixin,
                   GenericViewSet):
    
    """This viewset offers speciafily list method, returning dates in three list: 
    in_execution, if status project is in execution, not_in_execution and others
    """
    pass