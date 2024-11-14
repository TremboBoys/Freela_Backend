import mimetypes
import uuid
from django.db import models
import base64
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def image_file_path(image, _) -> str:
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
    file = models.ImageField(upload_to=image_file_path)
    description = models.CharField(max_length=255, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.description} - {self.attachment_key}"

    @property
    def url(self) -> str:
        file_url = self.file.url

        if default_storage.exists(self.file.name):
            with default_storage.open(self.file.name, "rb") as image_file:
                image_data = image_file.read()
                base64_encoded = base64.b64encode(image_data).decode("utf-8")
                return f"data:image/png;base64,{base64_encoded}"
        else:
            return "Image not found!"