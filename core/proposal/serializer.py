from rest_framework.serializers import ModelSerializer
from core.proposal.models import Proposal, Language, AcceptProposal

class ProposalSerializer(ModelSerializer):
    class Meta:
        model = Proposal
        fields = "__all__"
class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class AcceptProposalSerializer(ModelSerializer):
    class Meta:
        model = AcceptProposal
        fields = "__all__"
