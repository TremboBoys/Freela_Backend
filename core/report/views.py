from rest_framework.viewsets import ModelViewSet
from core.report.models import Report
from core.report.serializer import ReportSerializer

class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    
