from rest_framework.viewsets import ModelViewSet
from core.report.models import Report
from core.report.serializer import ReportSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from utils.viewset.report_view import ReportViewSet

class ReportViewSet(ReportViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
            




    



    
