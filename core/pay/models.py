from django.db import models
from core.perfil.models import Perfil

class City(models.Model):
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.city} - {self.state or 'No state'} - {self.country}"

class Address(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)    
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    
class Transaction(models.Model):
    id_transaction = models.CharField(max_length=255)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.id_transaction
        
    