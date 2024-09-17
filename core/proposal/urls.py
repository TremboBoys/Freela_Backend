from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.proposal.views import ProposalView, LanguageView, AcceptProposalView

router = DefaultRouter()
router.register(r"Proposal", ProposalView, basename="Proposal")
router.register(r"Language", LanguageView, basename="Language")
router.register(r"Accept", AcceptProposalView, basename="AcceptProposal")

urlpatterns = [
    path("", include(router.urls)),

]