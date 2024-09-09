from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.perfil.views import CategoriaFreelancerViewSet

router = DefaultRouter()
router.register(r"CategoriaFreelancer", CategoriaFreelancerViewSet, basename="CategoriaFreelancer")

urlpatterns = [
    path("", include(router.urls))
]