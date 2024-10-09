from django.apps import AppConfig


class AdsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.ads'

    def ready(self) -> None:
        import core.ads.signals.save_image
