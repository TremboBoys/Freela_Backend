from core.user.models import ForgetPassword, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from django.core.mail import send_mail
import random, requests

class ForgetPasswordView(APIView):
    def post(self, request):
        email = request.data['email']
        token = str(random.randint(100000, 999999))

        if User.objects.filter(email=email).exists:
            subject = request.POST.get("subject", "Reset password")
            message = request.POST.get("message", f"Your code for reset password: {token}\nLink for your reset password: ")
            recipient_list = [email]
            from_email = "martinsbarroskaua85@gmail.com"
            send_mail(
                subject,
                message,
                recipient_list=recipient_list,
                from_email=from_email
            )
            ForgetPassword.objects.create(email=email, token=token)

            return Response({"message": "Email enviado com sucesso"}, status=status.HTTP_200_OK)
        
class ResetPasswordView(APIView):
    def post(self, request):
        data = request.data

        if data['password']:
            passwordReset = ForgetPassword.objects.filter(token=data['token']).first()
            user = User.objects.filter(email=passwordReset.email).first()
            if not User:
                raise exceptions.NotFound("User not found")
            user.make_password(data['password'])
            user.save()
            passwordReset.delete()
            return Response({"message": "Update password!"})


    
        