from django.urls import path, include
from .use_case.send_token import SendToken
from core.user.views import UserAPIView


urlpatterns = [
    path("user/", UserAPIView.as_view(), name="user"),
    path("validationEmail", SendToken.as_view(), name='validationToken')
]