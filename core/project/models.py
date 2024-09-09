from django.db import models

class Project(models.Model):
    area = models.CharField(max_length=45)
    sub_area = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    subTitlte = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    context = models.CharField(max_length=45)
    demands = models.CharField(max_length=45)
    nivel_development = models.CharField(max_length=45)
    need_api_integration = models.CharField(max_length=45)
    need_frameworks = models.CharField(max_length=45)

    class NivelExperience(models.IntegerChoices):
        INICIANTE = 1, "Iniciante"
        INTERMEDIARIO = 2, "INTERMEDIARIO"
        EXPERIENTE = 3, "EXPERIENTE"
        ESPECIALISTA = 4, "ESPECIALISTA"

    experiente_required = models.IntegerField(("Experience"), choices=NivelExperience.choices, default=NivelExperience.INTERMEDIARIO)
    
    class Budget(models.IntegerChoices):
        MINIMAL = 1, "100 - 1000"
        MEDIUM = 2, "1000 - 5000"
        BIG = 3, "5000 - 10000"
        GIANT = 4, "10001 - 10000000000000000000000"
    budget = models.IntegerField(("Budget"), choices=Budget.choices, defaul=Budget.MEDIUM)

    class Size(models.IntegerChoices):
        SMALL = 1, "Small"
        MEDIUM = 2, "Medium"
        BIG = 3, "Big"
        GIANT = 4, "Giant"

    size = models.IntegerField(("Size"),choices=Size.choices, default=Size.MEDIUM)
    

