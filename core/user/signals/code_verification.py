from django.db.models.signals import post_save
from django.dispatch import receiver
from core.user.models import EmailVerification
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender=EmailVerification)
def send_code(sender, instance, created, **kwargs):
    subject = "Confirm your email"

    html_message = render_to_string('code_user.html', {
        'code': instance.code
    })
    text_content = strip_tags(html_message)
    recipient_list = [instance.email]
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
        print(f"Error in signal send code  in user {error}")
