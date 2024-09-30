from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.views import SendVericationCodeAPIView, UserAPIView, UserDeleteAPIView
router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("code/", SendVericationCodeAPIView.as_view(), name="code"),
    path("user/", UserAPIView.as_view(), name="user"),
    path("user/delete/<int:pk>", UserDeleteAPIView.as_view(), name="user")
]