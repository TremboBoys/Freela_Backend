from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.service.views import ContractServiceViewSet

router = DefaultRouter()
router.register("contract", ContractServiceViewSet, basename="contract")

urlpatterns = [
    path("", include(router.urls)),
]