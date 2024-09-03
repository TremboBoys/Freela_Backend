from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from django.core.mail import send_mail
from core.user.models import EmailVerified

class SendTokenAPIView(APIView):
    def post(self, request):
        data = request.data
        code = str(random.randint(100000, 999999))        
        subject = request.POST.get("subject", "Verify your email")
        message = request.POST.get("message", f"Use this code for verify your email: {code}")
        recipient_list = [data['email']]
        from_email = "martinsbarroskaua85@gmail.com"
        
        ema

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list
            )
            return Response({"message": "Sending email!"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Internal server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
