from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from core.service.models import ContractService
from core.perfil.models import Perfil


class CreateContractServiceMixim:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contractor = serializer.validated_data.get('contractor')
        user = contractor.user.type_user
        
        if user == 2:
            return Response({"message": "Freelancer can't contractor service"}, status=status.HTTP_410_GONE)
    
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
