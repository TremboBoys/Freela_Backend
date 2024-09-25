from django.dispatch import receiver
from django.db.models.signals import post_save
from core.report.models import Report
from core.report.use_case.report import generate_pdf
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Report)
def generate_report(sender, instance, **kwargs):
    try:
        freelancer_name = str(instance.accept_proposal.proposal.perfil.user.name)
        buffer = generate_pdf(
            title=str(instance.title), 
            text=str(instance.text_body), 
            name_freelancer=freelancer_name, 
            date_finished="10"
        )
        
        html_message = render_to_string('template/html/accept_email.html', {
            'name': f"Olá, o freelancer {freelancer_name} enviou um relatório"
        })
        
        subject = 'Relatório'
        recipient_list = [instance.accept_proposal.proposal.project.contractor.email]
        from_email = "martinsbarroskaua85@gmail.com"
        
        email = EmailMultiAlternatives(subject=subject, to=recipient_list, from_email=from_email)
        email.attach('report_{}.pdf'.format(instance.id), buffer.getvalue(), 'application/pdf')
        email.attach_alternative(html_message, "text/html")

        email.send()
        
    except Exception as error:
        logger.error(f"Erro ao gerar e enviar relatório: {error}")
