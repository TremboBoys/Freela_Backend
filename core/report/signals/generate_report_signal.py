from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from core.report.models import Report
from core.report.use_case.report import generate_pdf

@receiver(post_save, sender=Report)
def generateReport(sender, instance, **kwargs):
    print('erro no signal')
    generate_pdf(title=str(instance.title), text=str(instance.text_body), name_freelancer=str(instance.accept_proposal.proposal.perfil.user.name), date_finished="10")


    
    