from django.urls import path, include
from core.pay.views import CityAPIView

urlpatterns = [
    path("city", CityAPIView.as_view(), name="city")
]
