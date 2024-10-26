from django.db import models
from core.perfil.models import Perfil

class ContractService(models.Model):
    contractor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    class TypeOfService(models.IntegerChoices):
        FREE = 1, "FREE"
        MONTH = 2, "Month"
        YEAR = 3, "YEAR"
    type_of_service = models.IntegerField(("Type of user"), choices=TypeOfService.choices, default=TypeOfService.FREE)

