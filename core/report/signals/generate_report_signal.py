from django.dispatch import receiver
from django.db.models.signals import pre_save
from core.report.models import Report
from core.report.use_case.report import generate_pdf
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from core.report.use_case.ai_translate import ai_translate
from utils.mixins.report_mixin import ReportMixin

class ReportHandler(ReportMixin):
    pass

report_handler = ReportHandler()

@receiver(pre_save, sender=Report)
def generate_report(sender, instance, **kwargs):
    print("Estou sendo chamado!")
    instance = report_handler.process_instance(instance)
    language = instance.accept_proposal.proposal.language.name
    regular_text = instance.text_body
    title = instance.title
    print(instance.title, instance.text_body)

    new_text = ai_translate(text=regular_text, target_language=language)
    new_title = ai_translate(text=title, target_language=language)

    instance.text_body = new_text
    instance.title = new_title

    print(new_text, new_title)
    try:
        freelancer_name = str(instance.accept_proposal.proposal.perfil.user.name)

        buffer = generate_pdf(
            title=str(new_title), 
            text=str(new_text), 
            name_freelancer=freelancer_name, 
            price=instance.accept_proposal.proposal.price
        )

        html_message = render_to_string('html/accept_email.html', {
            'name': f'{instance.accept_proposal.proposal.perfil.user.email}',
            'id': f'{instance.id}',
        })
        text_content = strip_tags(html_message)
        subject = 'Relatório'
        recipient_list = [instance.accept_proposal.proposal.project.contractor.email]
        from_email = "martinsbarroskaua85@gmail.com"
        email = EmailMultiAlternatives(subject=subject, to=recipient_list, from_email=from_email, body=text_content)
        email.attach('report_{}.pdf'.format(instance.id), buffer.getvalue(), 'application/pdf')
        email.attach_alternative(html_message, "text/html")
        email.send()
    except Exception as error:
        print(f"Erro ao gerar e enviar relatório: {error}")
