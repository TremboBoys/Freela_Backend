from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.views import SendVericationCodeAPIView, UserAPIView
from core.user.authentication import LoginAPIView
router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("code/", SendVericationCodeAPIView.as_view(), name="code"),
    path("user/", UserAPIView.as_view(), name="user"),
    path("login/", LoginAPIView.as_view(), name='login')
]
