from django.apps import AppConfig


class PerfilConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.perfil'

    def ready(self) -> None:
        import core.perfil.signals.email_update