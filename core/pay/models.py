from django.db import models
from core.perfil.models import Perfil
from core.proposal.models import AcceptProposal
from core.service.models import ContractService
from core.ads.models import Ads
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
    cpf = models.CharField(max_length=11, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.cpf
class Transaction(models.Model):
    id_transaction = models.CharField(max_length=255)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    accept_proposal = models.ForeignKey(AcceptProposal, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(ContractService, on_delete=models.CASCADE, null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.id_transaction