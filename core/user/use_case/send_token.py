from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from core.user.models import User
import random
from rest_framework import status
from rest_framework.response import Response

@receiver(pre_save, sender=User)
def sendToken(sender, instance, request, **kwargs):
    if not instance.pk:
        token = str(random.randint(100000, 999999))
        message = request.POST.get("message", f"Use this token for verification: {token}")
        subject = request.POST.get("subject", "Confirm your email!")
        from_email = "martinsbarroskaua85@gmail.com"
        recipient_list = [instance.email]

        try:
            send_mail (
                message=message,
                subject=subject,
                recipient_list=recipient_list,
                from_email=from_email
            )
            instance.confirmation_token = token
            instance.is_active = False
            return Response({"message": "Send email with success"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        