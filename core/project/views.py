from rest_framework.viewsets import ModelViewSet
from core.project.serializer import ProjectSerializer
from core.project.models import Project
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail, send_mass_mail
from rest_framework.response import Response
from rest_framework import status
from core.perfil.models import Perfil
from django.core.mail import send_mass_mail
from rest_framework.response import Response
from core.perfil.models import Area

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
            try:
                id_area = Area.objects.get(name=instance.theme).pk
                print(id_area)
                users = Perfil.objects.filter(area=id_area)
                print(users)
                subject = 'Projeto do seu interesse'
                message = f'Ei, há um projeto que possa ser do seu interesse: {instance.title}'
                from_email = "martinsbarroskaua85@gmail.com"
                recipient_list = [user.user.email for user in users]
                print(recipient_list)
                send_mass_mail(
                    (recipient_list,
                    message,
                    from_email,
                    subject,
                    ),
                    fail_silently=False,
                )
                        
            except Area.DoesNotExist:
                return Response({"message": "Área não encontrada"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as error:
                return Response({"message": f"Houve um erro ao enviar o e-mail: {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                

            



