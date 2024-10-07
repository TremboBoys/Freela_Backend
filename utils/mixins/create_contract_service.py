from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings


class CreateContractServiceMixim:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        contractor = serializer.validated_data.get('contractor')
        print(contractor)
        type_user = contractor.perfil.user.type_user
        print(type_user)
        if type_user == 2:
            return Response({"message": "Admin or freelancer can't contract service"}, status=status.HTTP_410_GONE)

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
