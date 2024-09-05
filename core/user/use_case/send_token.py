from rest_framework.views import APIView
import random
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from core.user.models import EmailVerification
class SendToken(APIView):
    def post(self, request):
        code = str(random.randint(100000, 999999))
        email = request.data['email']
        
        message = request.POST.get('message', f'Code: {code}')
        subject = request.POST.get('subject', 'Confirm your email')
        from_email = "martinsbarroskaua85@gmail.com"
        recipient_list = [email]

        try: 
            newEmailVerification = EmailVerification.objects.create(email=email, code=code)
            newEmailVerification.save()

            send_mail (
                message=message,
                subject=subject,
                from_email=from_email,
                recipient_list=recipient_list
            )

            return Response({"message": "Email be sending"}, status=status.HTTP_201_CREATED)
        except BaseException as error:
            return Response({"message": f"Internal serverError: {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)