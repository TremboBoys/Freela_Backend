from rest_framework.viewsets import ModelViewSet, AcceptPurposeViewSet, PurposeViewSet
from core.proposal.serializer import ProposalSerializer, LanguageSerializer, AcceptProposalSerializer
from core.proposal.models import Proposal, Language, AcceptProposal
from rest_framework.response import Response
from rest_framework import status
class ProposalView(PurposeViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def list(self, request, *args, **kwargs):
        email_contratante = request.query_params.get('email', None)

        if not email_contratante:
            return Response({"message:": "O email do contrante é necessário"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset().filter(
            project__contractor__email =email_contratante
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class LanguageView(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class AcceptProposalView(AcceptPurposeViewSet):
    queryset = AcceptProposal.objects.all()
    serializer_class = AcceptProposalSerializer

        
    