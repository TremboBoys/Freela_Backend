
from core.proposal.models import Proposal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender=Proposal)
def newProposal(sender, instance, created, **kwargs):
    if created:
        subject = "Your project has new proposal!"
        recipient_list = [instance.project.contractor.email]
        from_email = "martinsbarroskaua85@gmail.com"
        html_message = render_to_string('new_proposal.html', {
            "name": instance.perfil.user.name.capitalize(),
            "value": instance.price,
            "delivery": instance.delivery
        })
        text_content = strip_tags(html_message)
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            to=recipient_list,
            from_email=from_email
            
        )
        
        try:
            email.attach_alternative(html_message, "text/html")
            email.send()
        except Exception as error:
            print(f"Has a error in sending email: {error}")