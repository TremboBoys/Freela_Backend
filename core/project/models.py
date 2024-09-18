from django.db import models
from core.user.models import User

class IntegrationType(models.Model):
    name = models.CharField(max_length=255)
class Project(models.Model):
    theme = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    class Function(models.IntegerChoices):
        WEB_DESIGN = 1, "Web_design"
        MOBILE_DESIGN = 2, "Mobile_design"
        MANAGER = 3, "Manager"
        OTHER = 4, "Other"
    function = models.IntegerField(("Function"), choices=Function.choices, default=Function.OTHER)
    class DevelopmentLevel(models.IntegerChoices):
        INIT = 1, "I don't have nothing"
        CONCEPT = 2, "I have a idea"
        READY  = 3, "I have a design"
    development_level = models.IntegerField("Level", choices=DevelopmentLevel.choices, default=DevelopmentLevel.INIT)
    class SpecialResource(models.IntegerChoices):
        YES = 1, "Yes"
        PERHAPS = 2, "Perhaps"
        NO = 3, "NO"
    special_resouce = models.IntegerField(('Special Resource'), choices=SpecialResource.choices, default=SpecialResource.NO)
    class ExperienceLevel(models.IntegerChoices):
        BEGINNER = 1, "Iniciante"
        INTERMEDIATE = 2, "Intermediário"
        EXPERIENCED = 3, "Experiente"
        EXPERT = 4, "Especialista"
    experience_level = models.IntegerField(choices=ExperienceLevel.choices,default=ExperienceLevel.BEGINNER)
    class ProjectSize(models.IntegerChoices):
        SMALL = 1, "Pequeno"
        MEDIUM = 2, "Intermediário"
        LARGE = 3, "Grande"
        GIANT = 4, "Gigante"
    project_size = models.IntegerField(choices=ProjectSize.choices, default=ProjectSize.SMALL)
    class BudgetRange(models.IntegerChoices):
        RANGE_100_1000 = 1, "R$100 - 1.000"
        RANGE_1000_5000 = 2, "R$1.000 - 5.000"
        RANGE_5000_10000 = 3, "R$5.000 - 10.000"
        OVER_10000 = 4, "Mais de R$10.000"
    budget_range = models.IntegerField(choices=BudgetRange.choices,default=BudgetRange.RANGE_100_1000)
    delivery = models.DateField(auto_now_add=True, null=True, blank=True)
    contractor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contractor")
    in_execution = models.BooleanField(default=False)
    class Status(models.IntegerChoices):
        NOT_STARTED = 1, "It project isn't started"
        PEDING = 2, "It project is pending"
        FINISHED = 3, "It project is pending"
    status = models.IntegerField(("Status of the project"), choices=Status.choices, default=Status.NOT_STARTED)
class ProjectIntegration(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    integration = models.ForeignKey(IntegrationType, on_delete=models.PROTECT)


    

