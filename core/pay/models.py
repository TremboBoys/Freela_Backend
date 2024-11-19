from django.db import models
from core.perfil.models import Perfil

class City(models.Model):
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.city} - {self.state or 'No state'} - {self.country}"

class Address(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    street_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    complemement = models.CharField(max_length=255, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    neighborhood_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    
    