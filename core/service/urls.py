from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.service.views import ContractServiceAPIView

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("service/", ContractServiceAPIView.as_view(), name="service")
]