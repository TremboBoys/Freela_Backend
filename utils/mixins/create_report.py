from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from core.proposal.models import AcceptProposal
from core.report.models import Report
class CreateReportModelModelMixin:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        accept_proposal = serializer.validated_data.get('accept_proposal')
        report = Report.objects.get(accept_proposal=accept_proposal)
        if not report.is_accept:        
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"message": "This project is finished"}, status=status.HTTP_410_GONE)
        

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
