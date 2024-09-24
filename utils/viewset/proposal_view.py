from utils.mixins.proposal_mixin import CreateProposalModelMixin
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class ProposalViewSet(CreateProposalModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    """
    This viewset provide speacily method create, but, 
    this method is conditioned for create proposal
    """
    pass