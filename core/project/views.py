from rest_framework.viewsets import ModelViewSet
from core.project.serializer import ProjectSerializer
from core.project.models import Project
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail, send_mass_mail
from rest_framework.response import Response
from rest_framework import status
from core.perfil.models import Perfil
class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @receiver(post_save, sender=Project)
    def sendEmailWhenCreate(sender, instance, created, **kwargs):
        if created:
            message = f"Ei, você cadastrou um novo projeto!"
            subject = "Novo projeto cadastrado"
            recipient_list = [instance.contractor.email]
            print(recipient_list)
            from_email = "martinsbarroskaua85@gmail.com"
            
            send_mail(
                subject=subject,
                message=message,
                recipient_list=recipient_list,
                from_email=from_email
            )

    @property
    def searchUser(projectType):
        users = Perfil.objects.get()
        

