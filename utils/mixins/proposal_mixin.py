from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings

class CreateProposalModelMixin:
    """
    Create a model instance, specify for proposalViewSet.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.validated_data.get('project')
        if project.in_execution:
            return Response({"message": "Esse projeto já está em execução!"}, status=status.HTTP_423_LOCKED)

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