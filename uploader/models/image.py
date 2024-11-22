import mimetypes
import uuid
from django.db import models
import base64
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def image_file_path(image, _):
    extension: str = mimetypes.guess_extension(image.file.file.content_type)
    if extension == ".jpe":
        extension = ".jpg"
    return f"images/{image.public_id}{extension or ''}"


class Image(models.Model):
    attachment_key = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        help_text="Used to attach the image to another object. Cannot be used to retrieve the image file.",
    )
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        help_text="Used to retrieve the image itself. Should not be readable until the image is attached to another object.",
    )
    file = models.ImageField(upload_to=image_file_path, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    image_base64 = models.TextField(blank=True, null=True, help_text="Store the base64 encoded image.")

    def __str__(self) -> str:
        return f"{self.description} - {self.attachment_key}"

    def save(self, *args, **kwargs):
        if self.file:
            super().save(*args, **kwargs)
            
            with open(self.file.path, "rb") as image_file:
                image_data = image_file.read()
                self.image_base64 = base64.b64encode(image_data).decode("utf-8")
        
        super().save(*args, **kwargs)

    @property
    def url(self) -> str:
        if self.image_base64:
            return f"data:image/png;base64,{self.image_base64}"
        elif self.file:
            return self.file.url 
        else:
            return "Image not found!"
