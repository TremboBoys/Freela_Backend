from core.proposal.models import Proposal
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Proposal)
def newProposal(sender, instance, created, **kwargs):
   if created:
    subject = "Seu projeto possui uma nova proposta"
    message = f"Olá, o usuário {instance.user.name} enviou uma proposta para você\nValor: R${instance.price}\nPrazo de entrega: {instance.delivery}"   
    recipient_list = [instance.project.contractor.email]
    from_email = "martinsbarroskaua85@gmail.com"

    send_mail (
        subject=subject,
        message=message,
        recipient_list=recipient_list,
        from_email=from_email,
    )