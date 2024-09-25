from django.dispatch import receiver
from django.db.models.signals import post_save
from core.report.models import Report
from core.report.use_case.report import generate_pdf
from django.core.mail import EmailMessage

@receiver(post_save, sender=Report)
def generateReport(sender, instance, **kwargs):
    try:
        buffer = generate_pdf(
            title=str(instance.title), 
            text=str(instance.text_body), 
            name_freelancer=str(instance.accept_proposal.proposal.perfil.user.name), 
            date_finished="10"
        )

        pdf_name = f"report_{instance.id}.pdf"
        
        subject = 'Relatório'
        message = f"Olá, o freelancer {instance.accept_proposal.proposal.perfil.user.name} enviou um relatório"
        recipient_list = [instance.accept_proposal.proposal.project.contractor.email]
        from_email = "martinsbarroskaua85@gmail.com"
        
        email = EmailMessage(subject=subject, body=message, from_email=from_email, to=recipient_list)

        email.attach(pdf_name, buffer.getvalue(), 'application/pdf')

        email.send()

    except Exception as error:
        print(f"Erro ao gerar ou enviar o PDF: {error}")