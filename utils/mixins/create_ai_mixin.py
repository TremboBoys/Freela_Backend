from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from utils.training_ai.request_ai import request_ai
from core.perfil.models import Perfil
import requests

class CreateAiModelMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        audience = serializer.validated_data.get('target_audience')
        category = serializer.validated_data.get('ads_category')
        headers = self.get_success_headers(serializer.data)
        
        # Chama a função request_ai que foi importada
        self.request_ai(audience, category)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        
    def request_ai(self, audience, category):
        for c in Perfil.objects.all():
            list_recommend = []
            data = {
                'audience': audience,
                'category': category.name,
                'area': c.area.name,
                'sub_area': c.sub_area.name
            }
            response = requests.post('http://127.0.0.1:8080/ai', json=data)
            
            if response.status_code != 200:
                print(f"Error in perfil request{c.id}: {response.status_code}")
                break
            else:
                response_json = response.json()  
                score = response_json['message'][0]['score'] 
                if score >= 0.961:
                    list_recommend.append(c.pk)
        print(list_recommend)
        return list_recommend   

