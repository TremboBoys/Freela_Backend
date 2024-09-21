from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from core.report.models import Report,Pdf
from core.report.use_case.report import generate_pdf
from uploader.models import Document
from rest_framework.response import Response
from rest_framework import status

@receiver(post_save, sender=Report)
def generateReport(sender, instance, **kwargs):
    try:
        generate_pdf(title=str(instance.title), text=str(instance.text_body), name_freelancer=str(instance.accept_proposal.proposal.perfil.user.name), date_finished="10")
    except BaseException as error:
        return Response({"message": f"Houve um erro dentro de receicer: {str(error)}"})
    