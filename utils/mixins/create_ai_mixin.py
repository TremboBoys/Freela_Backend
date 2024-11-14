from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from core.perfil.models import Perfil
import requests

class CreateAiModelMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        audience = serializer.validated_data.get('target_audience')
        category = serializer.validated_data.get('ads_category')
        headers = self.get_success_headers(serializer.data)
        
        self.request_ai(audience, category)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        
    def request_ai(audience, category):
        for c in Perfil.objects.all():
            data = {
                "audience": audience,
                "category": category,
                "area": c.area.name,
                "sub_area": c.sub_area.name
            }
            
            try:
                response = requests.post("http://127.0.0.1:8080/ai", json=data)
            except BaseException as error:
                return Response({"message": f"Error in request api: {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Has a error in api: {error}")
            
            
            
