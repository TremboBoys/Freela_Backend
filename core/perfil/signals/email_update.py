from django.db.models.signals import post_save
from core.perfil.models import Perfil
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.dispatch import receiver

@receiver(post_save, sender=Perfil)
def sendEmailUpdate(sender, instance, created, **kwargs):
        html_message = render_to_string('email_updated.html', {
                'name': instance.user.name.capitalize()
        })
        text_content = strip_tags(html_message)
        recipient_list = [instance.user.email]
        subject = "Your profile is update!"
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
            print(f"Has a error in send email: {error}")
            