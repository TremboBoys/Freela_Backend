from core.report.models import Report
from core.report.serializer import ReportSerializer
from utils.viewset.report_view import ReportViewSet

class ReportViewSet(ReportViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer