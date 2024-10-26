from core.perfil.models import Perfil
from core.project.models import Project
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mass_mail
from core.perfil.models import Area

def searchUser(projectType, projectName):
    try:
        id_area = Area.objects.get(name=projectType).pk
        users = Perfil.objects.filter(area=id_area)
        subject = 'Projeto do seu interesse'
        message = f'Ei, há um projeto que possa ser do seu interesse: {projectName}'
        from_email = "martinsbarroskaua85@gmail.com"
        recipient_list = [user.user.email for user in users]
        send_mass_mail(
            (subject, message, from_email, recipient_list),
            fail_silently=False,
        )
        
        return Response({"message": "E-mails enviados com sucesso."}, status=status.HTTP_200_OK)
    
    except Area.DoesNotExist:
        return Response({"message": "Área não encontrada."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        return Response({"message": f"Houve um erro ao enviar o e-mail: {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            