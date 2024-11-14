from django.apps import AppConfig


class MediaConfig(AppConfig):
    name = "uploader"
    
    def ready(self) -> None:
        import uploader.signals.updated_cloudinary 
