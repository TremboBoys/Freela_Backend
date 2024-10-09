from django.db import models
from uploader.models.image import Image
from core.perfil.models import Perfil

class Ads(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    links = models.URLField(max_length=255, blank=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

class AdsCategory(models.Model):
    name = models.CharField(max_length=255)