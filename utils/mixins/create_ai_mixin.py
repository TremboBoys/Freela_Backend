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
        image = serializer.validated_data.get('image')
        headers = self.get_success_headers(serializer.data)
        
        list_recommend = self.request_ai(audience, category.name)
        
        return Response({"message": f"{list_recommend, image}"}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        
    def request_ai(self, audience, category):
        list_recommend = []
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
                response = response.json()
                score = response['message'][0]['score']
                if score >= 0.92:
                    list_recommend.append(c.pk)
            else:
                print(f"Has a error in api: {error}")
        
        return list_recommend
            
            
            
