import requests
from django.core.files.base import ContentFile

def extract_pdf(url: str, model_instance: str | None, file_field_name: str | None):
    response = requests.get(url)

    if response.status_code == 200:
        file_name = url.split("/")[-1]
        file_content = ContentFile(response.content)

        pdf = getattr(model_instance, file_field_name).save(file_name, file_content)
        return pdf
    else:
        return f"Erro ao gerar o pdf"
