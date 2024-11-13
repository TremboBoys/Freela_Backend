from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from core.perfil.models import Perfil
#from transformers import pipeline
import requests

class CreateAiModelMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        audience = serializer.validated_data.get('target_audience')
        category = serializer.validated_data.get('ads_category')
        headers = self.get_success_headers(serializer.data)
        
        #self.request_ai(audience, category)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        
    """def request_ai(self, audience, category):
        #model_name = "KaliumPotas/potas_recommend"
        classifier = pipeline("text-classification", model=model_name)

        for c in Perfil.objects.all():
            list_recommend = []
            text = {
                'audience': audience,
                'category': category.name,
                'area': c.area.name,
                'sub_area': c.sub_area.name
            }
            result = classifier(text)
            
        print(result)    
        return result
    """
            
            
            
            
