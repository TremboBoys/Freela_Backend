from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.views import UserViewSet
from .use_case.send_token import SendToken
#from core.user.views import UserAPIView
#from .use_case.forget_password import ForgetPasswordView, ResetPasswordView
router = DefaultRouter()
router.register("user", UserViewSet, basename="Usr")

urlpatterns = [
    path("", include(router.urls)),
]