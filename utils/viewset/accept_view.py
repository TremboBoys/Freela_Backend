from rest_framework import mixins
from utils.mixins.accept_mixin import CreateAcceptProposalModelMixin
from rest_framework.viewsets import GenericViewSet

class AcceptProposalViewSet(CreateAcceptProposalModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):
    
    """
    This is similar the regular ModelViewSet, but implement a new mixin, 
    special for it
    """
    pass
