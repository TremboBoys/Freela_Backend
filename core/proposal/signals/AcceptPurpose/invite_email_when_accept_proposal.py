from core.proposal.models import AcceptProposal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender=AcceptProposal)
def accept_proposal_notification(sender, instance, created, **kwargs):
    if created:
        subject = "Your proproposal is accept!"
        
        html_message = render_to_string('proposal_accepted.html', {
            'project_title': instance.proposal.project.title,
        })
        text_content = strip_tags(html_message)
        recipient_list = [instance.proposal.perfil.user.email]
        from_email = "martinsbarroskaua85@gmail.com"

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            to=recipient_list,
            from_email=from_email,
        )
        
        try:
            email.attach_alternative(html_message, "text/html")
            email.send()
        except Exception as error:
            print(f"Error in signal accept proposal notification: {error}")
