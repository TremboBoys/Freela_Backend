from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.perfil.views import PerfilView

router = DefaultRouter()
router.register(r"perfil", PerfilView, basename="perfil")


urlpatterns = [
    path("", include(router.urls))
]