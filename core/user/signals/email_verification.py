from core.user.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(pre_save, sender=User)
def inviteEmail(sender, instance, **kwargs):
    email = instance.email  
    print(email)
    try:
        subject = f"Verification code"
        message = 'code'
        recipient_list = [email]
        from_email = "martinsbarroskaua85@gmail.com"
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=from_email,
            to=recipient_list,
        )
        email.send()
    except Exception as error:
        print(f"Erro in user signal: {error}")
    