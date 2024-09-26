from django.dispatch import receiver
from django.db.models.signals import post_save
from core.report.models import Report
from core.report.use_case.report import generate_pdf
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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
        
        print('A')
        html_message = render_to_string('html/accept_email.html', {
                'name': f'{instance.accept_proposal.proposal.perfil.user.email}',
                'id': f'{instance.id}'
        })
        print('B')
        text_content = strip_tags(html_message)
        print('c')
        subject = 'Relatório'
        recipient_list = [instance.accept_proposal.proposal.project.contractor.email]
        from_email = "martinsbarroskaua85@gmail.com"
        
        print('d')
        email = EmailMultiAlternatives(subject=subject, to=recipient_list, from_email=from_email, body=text_content)
        print('e')
        email.attach('report_{}.pdf'.format(instance.id), buffer.getvalue(), 'application/pdf')
        print('f')
        email.attach_alternative(html_message, "text/html")
        print("G")
        email.send()
        print('H')
    except Exception as error:
        print(f"Erro ao gerar e enviar relatório: {error}")
