from django.apps import AppConfig


class ReportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.report'

    #def ready(self):
    #    import core.report.signals.generate_report_signal