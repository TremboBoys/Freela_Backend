from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from utils.mixins.create_report import CreateReportModelModelMixin
from utils.mixins.update_report import UpdateReportModelMixin

class ReportViewSet(CreateReportModelModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    UpdateReportModelMixin,
                    GenericViewSet):
    pass