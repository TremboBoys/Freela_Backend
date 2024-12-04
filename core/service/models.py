from django.db import models
from core.perfil.models import Perfil
from datetime import timedelta
from django.utils.timezone import now

class ContractService(models.Model):
    contractor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    class TypeOfService(models.IntegerChoices):
        FREE = 1, "FREE"
        MONTH = 2, "Month"
        YEAR = 3, "YEAR"
    type_of_service = models.IntegerField(("Type of user"), choices=TypeOfService.choices, default=TypeOfService.FREE)
    is_paid = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def cancel_payment(self, *args, **kwargs):
        if now() - self.created_at == 30 and self.is_paid == True:
            self.is_paid = False
            self.save()