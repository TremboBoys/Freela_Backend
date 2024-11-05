from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.views import UserAPIView, SendCode
from core.user.authentication import LoginAPIView
router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("user/", UserAPIView.as_view(), name="user"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("code/", SendCode.as_view(), name="code"),
]
