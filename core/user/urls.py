from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.views import UserAPIView
router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("user/", UserAPIView.as_view(), name="user"),
]
