from core.user.models import ForgetPassword, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from django.core.mail import send_mail
import random
from django.contrib.auth.hashers import make_password

class ForgetPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        token = str(random.randint(100000, 999999))

        # Verifica se o usuário existe
        if User.objects.filter(email=email).exists():
            subject = request.data.get("subject", "Reset password")
            message = request.data.get("message", f"Your code for reset password: {token}\nLink for your reset password: ")
            recipient_list = [email]
            from_email = "martinsbarroskaua85@gmail.com"
            send_mail(
                subject,
                message,
                from_email,
                recipient_list
            )
            ForgetPassword.objects.create(email=email, token=token)

            return Response({"message": "Email enviado com sucesso"}, status=status.HTTP_200_OK)
        
        return Response({"error": "Email não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
class ResetPasswordView(APIView):
    def post(self, request):
        data = request.data
        password = data.get('password')
        token = data.get('token')

        if password and token:
            password_reset = ForgetPassword.objects.filter(token=token).first()
            if not password_reset:
                raise exceptions.NotFound("Token inválido ou expirado")
            
            user = User.objects.filter(email=password_reset.email).first()
            if not user:
                raise exceptions.NotFound("Usuário não encontrado")
            
            user.password = make_password(password)
            user.save()
            
            password_reset.delete()
            return Response({"message": "Senha atualizada com sucesso!"}, status=status.HTTP_200_OK)

        return Response({"error": "Dados inválidos"}, status=status.HTTP_400_BAD_REQUEST)
