from django.db import models
from core.perfil.models import Perfil
from core.proposal.models import AcceptProposal
from uploader.models.document import document_file_path


class Report(models.Model):
    title = models.CharField(max_length=255)
    text_body = models.CharField(max_length=255)
    accept_proposal = models.ForeignKey(AcceptProposal, on_delete=models.CASCADE)
    is_accept = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"{self.title} - {self.text_body}"
class Pdf(models.Model):
    report = models.FileField(upload_to=document_file_path)
    

    
    