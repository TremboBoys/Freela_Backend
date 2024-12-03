from io import StringIO
import uuid
from django.db import models
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
        
cloudinary.config(
    cloud_name="dm2odcrnf",
    api_key="392291948516824",
    api_secret="8L8ApfYnDq6_YiXSd4lAgDmZGnI",
)



class Image(models.Model):
    attachment_key = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        help_text="Used to attach the image to another object. Cannot be used to retrieve the image file.",
    )
    public_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        unique=True,
        help_text="Public ID from Cloudinary, used to retrieve the image file.",
    )
    file = models.ImageField(upload_to="image/", blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.description} - {self.attachment_key}"

    def save(self, *args, **kwargs):
        if self.file and not self.public_id:
            if hasattr(self.file.file, "size") and self.file.file.size > 0:
                upload_result = upload(self.file.file, folder="images/")
                self.public_id = upload_result.get("public_id")
            else:
                raise ValueError("Cannot upload an empty file.")

        super().save(*args, **kwargs)

    @property
    def url(self) -> str:
        if self.public_id:
            url, _ = cloudinary_url(self.public_id)
            return url
        else:
            return "Image not found"
