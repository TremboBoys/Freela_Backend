from django.dispatch import receiver
from django.db.models.signals import post_save
from core.ads.models import Ads
import cloudinary, cloudinary.uploader, cloudinary.api

@receiver(post_save, sender=Ads)
def uploadImageInCloudinary(sender, instance, created, **kwargs):
    if created:
        try:
            result = cloudinary.uploader.upload(instance.image.file)
        except Exception as error:
            print("Has a error in upload image", error)
        print("Image uploaded")
        
