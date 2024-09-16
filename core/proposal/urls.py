from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.proposal.views import ProposalView, LanguageView

router = DefaultRouter()
router.register(r"Proposal", ProposalView, basename="Proposal")
router.register(r"Language", LanguageView, basename="Language")

urlpatterns = [
    path("", include(router.urls)),

]