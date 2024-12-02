from rest_framework.routers import DefaultRouter
from django.urls import path, include

from uploader import views

app_name = "uploader"

router = DefaultRouter()
router.register("images", views.ImageUploadViewSet)
router.register("documents", views.DocumentUploadViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


