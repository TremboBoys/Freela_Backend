from django.db import models
from core.project.models import Project
from core.user.models import User

class CategoriaFreelancer(models.Model):
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name
    
class MyProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    class Status(models.IntegerChoices):
        PENDING = 1, "Pending"
        FINSHED = 2, "Finished"
    status = models.IntegerField(('status'), choices=Status.choices, default=Status.PENDING)
    term = models.DateTimeField()
    
class Hability(models.Model):
    hability = models.CharField(max_length=45)

class MyHability(models.Model):
    user_hability = models.ForeignKey(Hability, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
class Perfil(models.Model):
    balance = models.CharField(max_length=45)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    price_per_hour = models.DecimalField(decimal_places=2, max_digits=9999999999999999)
    is_public = models.BooleanField(default=True)
    about_me = models.CharField(max_length=255)
    category_Feelance = models.ForeignKey(CategoriaFreelancer, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.balance} - {self.about_me}"



