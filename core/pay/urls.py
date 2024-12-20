from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.pay.views import CityViewSet, AddressAPIView, TransactionAPIView

router = DefaultRouter()
router.register("city", CityViewSet, basename="city")

urlpatterns = [
    path("", include(router.urls)),
    path("address/", AddressAPIView.as_view(), name="address"),
    path("transaction", TransactionAPIView.as_view(), name="transaction")
]
