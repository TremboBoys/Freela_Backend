from django.db import models
from core.user.models import User
from core.perfil.models import Area
from core.perfil.models import SubArea
from core.perfil.models import Perfil
from core.perfil.models import MyCompetency
from core.project.models import Project

class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Proposal(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    sub_area = models.ForeignKey(SubArea, on_delete=models.CASCADE) 
    price = models.DecimalField(decimal_places=2, max_digits=12)
    class PaymentType(models.IntegerChoices):
        PIX = 1, "Pix"
        DEBIT = 2, "Debit"
        CREDIT = 3, "Credit"

    payement_type = models.IntegerField(("Pix"), choices=PaymentType.choices, default=PaymentType.PIX)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    my_competency = models.ForeignKey(MyCompetency, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
class AcceptProposal(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    


