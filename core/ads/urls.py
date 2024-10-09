from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.ads.views import AdsViewSet, AdsCategoryViewSet


router = DefaultRouter()
router.register("ads", AdsViewSet, basename="ads")
router.register("ads-category", AdsCategoryViewSet, basename="ads-category")

urlpatterns = [
    path("", include(router.urls))
]