from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.pay.views import CityViewSet, AddressAPIView, NotificationAPIView

router = DefaultRouter()
router.register("city", CityViewSet, basename="city")

urlpatterns = [
    path("", include(router.urls)),
    path("address/", AddressAPIView.as_view(), name="address"),
    path("notification/", NotificationAPIView.as_view, name="notfication")
]
