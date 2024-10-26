from django.contrib import admin
from core.proposal.models import Proposal, Language, AcceptProposal


admin.site.register(Proposal)
admin.site.register(Language)
admin.site.register(AcceptProposal)