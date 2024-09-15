from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.project.views import ProjectView

router = DefaultRouter()
router.register(r"Projetos", ProjectView, basename="Projetos")

urlpatterns = [
    path("", include(router.urls))
]