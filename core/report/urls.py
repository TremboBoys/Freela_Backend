from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.report.views import ReportViewSet
router = DefaultRouter()
router.register(r"Report", ReportViewSet, basename="Report")

urlpatterns = [
    path("", include(router.urls)),
]