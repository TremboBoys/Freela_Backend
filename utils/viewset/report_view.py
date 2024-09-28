from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from utils.mixins.create_report import CreateReportModelModelMixin

class ReportViewSet(CreateReportModelModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):
    pass