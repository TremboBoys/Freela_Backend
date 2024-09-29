from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.report.views import ReportViewSet
from core.report.views import TranslationAPIView
router = DefaultRouter()
router.register(r"Report", ReportViewSet, basename="Report")

urlpatterns = [
    path("", include(router.urls)),
    path("translation", TranslationAPIView.as_view(), name='translate')
]