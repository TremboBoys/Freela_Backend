from core.project.models import Project
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.perfil.models import Perfil, Area
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@receiver(post_save, sender=Project)
def filter_theme_area(sender, instance, created, **kwargs):
    if created:
        filter_list = [instance.theme, instance.context, instance.description]
        area = None

        for field_value in filter_list:
            try:
                area = Area.objects.get(name=field_value)
                print(area)
                break  
            except Area.DoesNotExist:
                print('1')
                continue

        if area:
            recipient_list = [
                perfil.user.email for perfil in Perfil.objects.filter(area=area)
            ]
            print(recipient_list)
            if recipient_list:
                html_message = render_to_string('bot_template.html', {
                    'title': instance.title,
                })
                text_content = strip_tags(html_message)
                from_email = "martinsbarroskaua85@gmail.com"
                subject = "There's a project that may interest you!"

                email = EmailMultiAlternatives(
                    subject=subject,
                    body=text_content,
                    to=recipient_list,
                    from_email=from_email,
                )

                try:
                    email.attach_alternative(html_message, "text/html")
                    print('jsjalka')
                    email.send()
                    print('email enviado')
                except Exception as error:
                    print(f"Error in sending project notification email: {error}")
