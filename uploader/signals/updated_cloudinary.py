from django.db.models.signals import post_save
from django.dispatch import receiver
from uploader.models.image import Image
import cloudinary, cloudinary.uploader, cloudinary.api


@receiver(post_save, sender=Image)
def save_in_cloudinary(instance, created, sender, kwargs):
    if created:
        image = instance.file
        pass
        