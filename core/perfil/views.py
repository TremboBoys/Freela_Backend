from rest_framework.viewsets import ModelViewSet 
from core.perfil.serializer import PerfilSerializer, ProSerializer, MyCompetencySerializer, MyProjectSerializer, NacionalitySerializer, AreaSerializer,SubAreaSerializer, HabilitySerializer
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from core.perfil.models import Perfil, Pro, MyProjects, MyCompetency, Hability, Area, SubArea, Nacionality
from core.user.models import User
from rest_framework.response import Response
from rest_framework import status

class PerfilView(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

    @receiver(post_save, sender=Perfil)
    def sendEmailUpdate(sender, instance, created, **kwargs):
        message = "Seu perfil foi alterado"
        subject = f"Olá {instance.user.name}!, se perfil sofreu algumas alterações!"
        recipient_list = [instance.user.email]
        from_email = "martinsbarroskaua85@gmail.com"
        if not created:
            send_mail(
                message=message,
                subject=subject,
                recipient_list=recipient_list,
                from_email=from_email
            )

    

class ProView(ModelViewSet):
    queryset = Pro.objects.all()
    serializer_class = ProSerializer

class NacionalityView(ModelViewSet):
    queryset = Nacionality.objects.all()
    serializer_class = NacionalitySerializer

class AreaView(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class SubAreaView(ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer

class HabilityView(ModelViewSet):
    queryset = Hability.objects.all()
    serializer_class = HabilitySerializer

from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class MyProjectsView(ModelViewSet):
    queryset = MyProjects.objects.all()
    serializer_class = MyProjectSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        previous_in_execution = instance.in_execution
        if instance.in_execution  =True:
            response = super().update(request, *args, **kwargs)
            subject = f"O projeto {instance.project.title} está finalizado"
            message = f"Olá {instance.project.contractor}, seu projeto está finalizado"
            recipient_list = [instance.project.contractor.user.email]
            from_email = "martinsbarroskaua85@gmail.com"
            send_mail(
                message=message,
                subject=subject,
                recipient_list=recipient_list,
                from_email=from_email
            )
            return Response({"message": "Deu tudo certo"}, status=status.HTTP_200_OK)
        elif instance.in_execution:
            return Response({"message": "Então bro, seguinte, para de cagar"}, status=status.HTTP_400_BAD_REQUEST)
class MyCompetencyView(ModelViewSet):
    queryset = MyCompetency.objects.all()
    serializer_class = MyCompetencySerializer
