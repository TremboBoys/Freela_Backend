from django.urls import path, include
from core.pay.views import CityAPIView, AddressAPIView

urlpatterns = [
    path("city", CityAPIView.as_view(), name="city"),
    path("address", AddressAPIView.as_view(), name="address"),
]
