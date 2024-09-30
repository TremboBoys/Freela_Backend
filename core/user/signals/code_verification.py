from django.db.models.signals import post_save
from django.dispatch import receiver
from core.user.models import EmailVerification
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=EmailVerification)
def send_code(sender, instance, created, **kwargs):
    if created:
        try:
            subject = "Confirm your email"
            message = f"Your code {instance.code}"
            recipient_list = [instance.email]
            from_email = "martinsbarroskaua85@gmail.com"
            email = EmailMultiAlternatives(
                subject=subject,
                body=message,
                to=recipient_list,
                from_email=from_email,
            )
            email.send()
        except Exception as error:
            print(f"Error in signal send code  in user {error}")
