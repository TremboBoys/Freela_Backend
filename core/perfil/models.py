from core.user.models import User
from django.db import models

class Nacionality(models.Model):
    name = models.CharField(max_length=45);

    def __str__(self) -> str:
        return self.name
    
class Perfil(models.Model):
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User.email, on_delete=models.PROTECT)
    price_per_hour = models.DecimalField(decimal_places=2, max_digits=20)
    nacionality = models.ForeignKey(Nacionality, on_delete=models.PROTECT)
    class PaymentType(models.IntegerChoices):
        PIX = 1, "Pix"
        DEBITO = 2, "Debito"
        CREDITO = 3, "Credito"
    payment_type = models.IntegerChoices(("Payment type"), choices=PaymentType.choices, default=PaymentType.PIX)
    