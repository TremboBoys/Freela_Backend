from core.user.models import User
from django.db import models    
from django.db.models import Sum, Avg
from core.project.models import Project
from uploader.models.document import Document
from uploader.models.image import Image
from cloudinary.utils import cloudinary_url


class Nacionality(models.Model):
    name = models.CharField(max_length=45)
    def __str__(self) -> str:
        return self.name
class Hability(models.Model):
    name = models.CharField(max_length=45)
     
    def __str__(self) -> str:
        return self.name 
class Area(models.Model):
    name = models.CharField(max_length=45)
    
    def __str__(self) -> str:
        return self.name
class SubArea(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name
class Perfil(models.Model):
    balance = models.DecimalField(decimal_places=2, max_digits=11)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    price_per_hour = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    nacionality = models.ForeignKey(Nacionality, on_delete=models.CASCADE, related_name="nacionality")
    #photo = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="photo", null=True, blank=True)
    class PaymentType(models.IntegerChoices):
        PIX = 1, "Pix"
        DEBITO = 2, "Debito"
        CREDITO = 3, "Credito"
    payment_type = models.IntegerField(("Payment type"), choices=PaymentType.choices, default=PaymentType.PIX)
    about_me = models.CharField(max_length=255, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="area", null=True, blank=True)
    sub_area = models.ForeignKey(SubArea, on_delete=models.CASCADE, related_name="sub_area")
    number_projects_in_execution = models.IntegerField(null=True, blank=True)
    is_pro = models.BooleanField(default=False, null=True, blank=True)
    access_token_mercado_pago = models.CharField(max_length=255, null=True, blank=True)
    refresh_token_mercado_pago = models.CharField(max_length=255, null=True, blank=True)
    expiration_date_access_token_mercado_pago = models.CharField(max_length=255, null=True, blank=True)
    expiration_date_refresh_token_mercado_pago = models.CharField(max_length=255, null=True, blank=True)
    collector_id_mercado_pago = models.CharField(max_length=255, null=True, blank=True)
    avaliation = models.IntegerField(null=True, blank=True)
    every_avaliations = models.IntegerField(null=True, blank=True)
    image_perfil = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.about_me} - {self.balance}"
    
class MyCompetency(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    my_hability = models.ForeignKey(Hability, on_delete=models.CASCADE)
    class Time(models.IntegerChoices):
        LITTLE = 1, "1"
        NORMAL = 2, "1 - 3"
        HIGH = 3, "3 - 5"
        LOT = 4, "5 - more"
    time = models.IntegerField(("Time of experience"), choices=Time.choices, default=Time.NORMAL)
    service = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    certification = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
class MyProjects(models.Model):
    in_execution = models.BooleanField(default=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="perfil")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project")
class Pro(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    become_pro = models.DateField()
    is_paid = models.BooleanField(default=False)

class ChoiceProject(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    project = models.ForeignKey(MyProjects, on_delete=models.CASCADE)
    
class PerfilAvaliation(models.Model):
    perfil_avaliator = models.ForeignKey(
        Perfil, 
        on_delete=models.CASCADE, 
        related_name='given_evaluations' 
    )
    perfil_receiver = models.ForeignKey(
        Perfil, 
        on_delete=models.CASCADE, 
        related_name='received_evaluations'  
    )
    star_number = models.IntegerField()