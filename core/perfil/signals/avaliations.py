from django.dispatch import receiver
from django.db.models.signals import post_save
from core.perfil.models import PerfilAvaliation
from django.db import models

@receiver(post_save, sender=PerfilAvaliation)
def updateAvaliations(sender, instance, created, **kwargs):
    print('Estou sendo chamado')
    if created:
        perfil_receiver = instance.perfil_receiver
        total_stars = PerfilAvaliation.objects.filter(perfil_receiver=perfil_receiver).aggregate(
            total_stars=models.Sum('star_number')
        )['total_stars'] or 0
        total_aval = PerfilAvaliation.objects.filter(perfil_receiver=perfil_receiver).count()

        perfil_receiver.avaliation = total_stars / total_aval if total_aval > 0 else 0
        perfil_receiver.every_avaliations = total_aval
        perfil_receiver.save()
        print('Fui finalizado')

