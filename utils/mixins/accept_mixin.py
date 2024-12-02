from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings

class CreateAcceptProposalModelMixin:
    """
    Regular mixim, but with specificy validation
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        proposal = serializer.validated_data.get('proposal')
        if proposal.project.in_execution == True:
            return Response({"message": "Uma proposta para esse projeto já foi aceita"}, status=status.HTTP_423_LOCKED)
            
        else:
            proposal.project.in_execution = True
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