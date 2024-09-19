from django.db import models
from core.perfil.models import Perfil
from core.proposal.models import AcceptProposal


class Report(models.Model):
    title = models.CharField(max_length=255)
    text_body = models.CharField(max_length=255)
    date = models.DateField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    accept_proposal = models.ForeignKey(AcceptProposal, on_delete=models.CASCADE)
    is_accept = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} - {self.text_body}"
    
    