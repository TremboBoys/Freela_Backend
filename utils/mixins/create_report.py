from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from core.report.models import Report

class CreateReportModelModelMixin:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        accept_proposal = serializer.validated_data.get('accept_proposal')

        report = Report.objects.filter(accept_proposal=accept_proposal)

        for values in report:
            if values.is_accept == True:
                return Response({"message": "Não é possível gerar novos relatórios para este projeto."}, status=status.HTTP_410_GONE)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        



