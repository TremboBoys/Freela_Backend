from django.dispatch import receiver
from django.db.models.signals import post_save
from core.report.models import Report
from core.report.use_case.report import generate_pdf
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status

@receiver(post_save, sender=Report)
def generateReport(sender, instance, **kwargs):
    try:
        freelancer_name = str(instance.accept_proposal.proposal.perfil.user.name)
        buffer = generate_pdf(
            title=str(instance.title), 
            text=str(instance.text_body), 
            name_freelancer=freelancer_name, 
            date_finished="10"
        )
        print("PÉ")
        pdf_name = f"report_{instance.id}.pdf"
        try:
            html_message = render_to_string('template/html/accept_email.html', {
                'name': f"Olá, o freelancer {freelancer_name} enviou um relatório"
            })
            print('kjadajl')
        except BaseException as error:
            print(error)                
        print("PÁ")
        subject = 'Relatório'
        recipient_list = [instance.accept_proposal.proposal.project.contractor.email]
        from_email = "martinsbarroskaua85@gmail.com"
    
        email = EmailMessage(subject=subject, body=html_message, from_email=from_email, to=recipient_list)
        email.attach(pdf_name, buffer.getvalue(), 'application/pdf')

        email.send()
        
    except Exception as error:
        return Response({"message": f"{error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
