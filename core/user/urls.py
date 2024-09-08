from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.views import UserView
from .use_case.forget_password import ForgetPasswordView, ResetPasswordView
router = DefaultRouter()
router.register(r"User", UserView, basename="User")

urlpatterns = [
    path("", include(router.urls)),
    path("Forget/", ForgetPasswordView.as_view(), name="requestForgetPassowrd"),
    path("Reset/", ResetPasswordView.as_view(), name="resetPassowrd")
]