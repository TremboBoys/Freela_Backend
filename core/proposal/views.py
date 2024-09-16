from rest_framework.viewsets import ModelViewSet
from core.proposal.serializer import ProposalSerializer, LanguageSerializer
from core.proposal.models import Proposal, Language

class ProposalView(ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

class LanguageView(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer