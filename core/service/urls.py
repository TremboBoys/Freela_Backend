from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.service.views import ServiceViewSet

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")

urlpatterns = [
    path("", include(router.urls))
]