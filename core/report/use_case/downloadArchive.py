import cloudinary.api
import requests
from django.core.files.base import ContentFile
import cloudinary
from config.settings import cl

def extract_pdf(url):
    print(url)
    print("beta broxa")
    response = cloudinary.api()
    if response.status_code == 200:
        print("200")
    else:
        print('pizza')

    return response