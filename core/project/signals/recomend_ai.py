from core.perfil.models import Perfil
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.project.models import Project
import requests

@receiver(post_save, sender=Project)
def ai_recommend(instance, sender, created, **kwargs):
    list_recommend = []
    if created:
        for c in Perfil.objects.all():
            request_json = {
                "audience": instance.description,
                "category": instance.theme,
                "area": c.area.name,
                "sub_area": c.sub_area.name
            } 
            try:
                response = requests.post(f"http://127.0.0.1:8080/ai", json=request_json)
                response.raise_for_status()  
            except requests.exceptions.ConnectionError as error:
                print(f"AI recommend service encountered a problem: {error}")
                continue
            except requests.exceptions.HTTPError as http_error:
                print(f"HTTP error occurred: {http_error}")
                continue

            if response.status_code == 200:
                response_data = response.json()
                score = response_data.get('message', [{}])[0].get('score', -1.0)
                if score >= 0.9:
                    list_recommend.append(c.pk)

        instance.response_ai = list_recommend
        instance.save()
