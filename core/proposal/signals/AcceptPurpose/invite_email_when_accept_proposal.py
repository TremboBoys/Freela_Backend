
from core.proposal.models import AcceptProposal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save, sender=AcceptProposal)
def acceptPurpose(instance, created, *args, **kwargs):
    if created:
        subject = f"Sua proposta foi aceita!"
        message = f"Olá {instance.proposal.perfil.user.email}, sua proposta para o projeto para o projeto: {instance.proposal.project.title} foi aceita!!!!!!"
        recipient_list = [instance.proposal.project.contractor.email]
        from_email = "martinsbarroskaua85@gmail.com"
        send_mail(
             recipient_list=recipient_list,
            message=message,
            subject=subject, 
            from_email=from_email
        )
                   