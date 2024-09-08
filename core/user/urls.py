from django.urls import path, include
from .use_case.send_token import SendToken
from core.user.views import UserAPIView
from .use_case.forget_password import ForgetPasswordView, ResetPasswordView

urlpatterns = [
    path("", include(router.urls)),
    path("Forget/", ForgetPasswordView.as_view(), name="requestForgetPassowrd"),
    path("Reset/", ResetPasswordView.as_view(), name="resetPassowrd"),
    path("user/", UserAPIView.as_view(), name="user"),
    path("validationEmail", SendToken.as_view(), name='validationToken'),
]