from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from core.perfil.models import Perfil
from uploader.models.image import Image
import requests

class CreateServiceModelMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        context = serializer.validated_data.get('context')
        description = serializer.validated_data.get('description')
        headers = self.get_success_headers(serializer.data)
        
        list_recommend = self.ai_service(context=context, description=description)
        
        resp = {
            "message": "Project created!",
            "datas of project": serializer.data,
            "recommend this service for theirs": list_recommend
        }
        
        return Response(resp, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        
    def ai_service(self, context, description):
        list_recommend = []
        for c in Perfil.objects.all():
            data = {
                "audience": context,
                "category": description,
                "area": c.area.name,
                "sub_area": c.sub_area.name
            }
            try:
                response = requests.post('http://127.0.0.1:8080/ai/', json=data)
            except Exception as error:
                print(f"Error in AI for service: {error}")
                
            if response.status_code == 200:
                resp = response.json()
                score = resp['message'][0]['score']
                print(score)
                
                if score >= 0.85:
                    list_recommend.append(c.pk)
            else:
                print("There's a error in connection with AI")            
            return list_recommend
            