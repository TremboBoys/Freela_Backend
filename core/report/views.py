from rest_framework.viewsets import ModelViewSet
from core.report.models import Report
from core.report.serializer import ReportSerializer
from rest_framework.decorators import action

class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    



    
