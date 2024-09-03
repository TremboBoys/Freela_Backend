from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.views import UserView

router = DefaultRouter()
router.register(r"User", UserView, basename="User")

urlpatterns = [
    path("", include(router.urls))
]