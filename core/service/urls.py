from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.service.views import ServiceViewSet, ContractServiceViewSet

router = DefaultRouter()
router.register("service", ServiceViewSet, basename="service")
router.register("contract", ContractServiceViewSet, basename="contract")


urlpatterns = [
    path("", include(router.urls))  
]