from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from utils.mixins.create_report import CreateReportModelModelMixin
from utils.mixins.update_report import UpdateReportModelMixin
from utils.mixins.get_report import ListReportModelMixin

class ReportViewSet(CreateReportModelModelMixin,
                    ListReportModelMixin,
                    mixins.RetrieveModelMixin,
                    UpdateReportModelMixin,
                    GenericViewSet):
    pass