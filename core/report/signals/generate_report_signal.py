from django.dispatch import receiver
from django.db.models.signals import pre_save
from core.report.models import Report
from core.report.use_case.report import generate_pdf

@receiver(pre_save, sender=Report)
def generateReport(sender, instance, **kwargs):
    generate_pdf(title=instance.title, text=instance.text_body, price=instance.accept_proposal.proposal.price, name_freelancer=instance.accept_proposal.proposal.perfil.user.name, date_finished=10)


    
    