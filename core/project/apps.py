from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.project'

    def ready(self):
        import core.project.signals.projectView.send_email_and_filter_when_added
