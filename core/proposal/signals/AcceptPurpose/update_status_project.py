from core.proposal.models import  AcceptProposal
from django.db.models.signals import  pre_save
from django.dispatch import receiver
from core.project.models import Project
from core.perfil.models import MyProjects

@receiver(pre_save, sender=AcceptProposal)
def updateStatusProject(instance, sender, **kwargs):
    newProjects = MyProjects.objects.create(perfil=instance.proposal.perfil, project=instance.proposal.project, in_execution=True)
    newProjects.save()
    Project.objects.filter(id=instance.proposal.project.pk).update(in_execution=True)