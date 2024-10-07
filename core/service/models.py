from django.db import models
from core.perfil.models import Perfil

class Service(models.Model):
    class TypeOfService(models.IntegerChoices):
        FREE = 1, "Free"
        MONTH = 2, "Month"
        YEAR = 3, "Year"
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    service = models.IntegerField(("Services"), choices=TypeOfService.choices, default=TypeOfService.FREE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
class ContractService(models.Model):
    contractor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)