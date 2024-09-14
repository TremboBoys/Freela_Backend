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
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        old_value = instance.in_execution

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        new_value = instance.in_execution

        
        if new_value == False and new_value != old_value:
            print(instance.project.contractor.user)
            subject = f"O projeto {instance.project.title} está finalizado"
            message = f"Olá {instance.project.contractor.name}, seu projeto está finalizado"
            recipient_list = [instance.project.contractor.email]
            from_email = "martinsbarroskaua85@gmail.com"
            send_mail(
                message=message,
                subject=subject,
                recipient_list=recipient_list,
                from_email=from_email
            )
        return Response(serializer.data)
class MyCompetencyView(ModelViewSet):
    queryset = MyCompetency.objects.all()
    serializer_class = MyCompetencySerializer
