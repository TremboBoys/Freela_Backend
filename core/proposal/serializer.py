from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.proposal.models import Proposal, Language

class ProposalSerializer(ModelSerializer):
    class Meta:
        model = Proposal
        fields = "__all__"

class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"