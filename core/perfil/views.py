from rest_framework.viewsets import ModelViewSet 
from core.perfil.models import Perfil
from core.perfil.serializer import PerfilSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from core.perfil.models import Perfil
from core.user.models import User

class PerfilView(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

    @receiver(post_save, sender=Perfil)
    def sendEmailUpdate(sender, request, instance, created, **kwargs):
        message = request.POST.get("message", "Seu perfil foi alterado")
        subject = request.POST.get("subject", f"Olá {instance.user.name}!, se perfil sofreu algumas alterações!")
        recipient_list = [instance.user.email]
        from_email = "martinsbarroskaua85@gmail.com"
        if not created:
            send_mail(
                message=message,
                subject=subject,
                recipient_list=recipient_list,
                from_email=from_email
            )



