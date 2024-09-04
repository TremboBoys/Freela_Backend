from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    password= models.CharField(max_length=45)
    confirmation_token = models.CharField(max_length=6, blank=True, null=True)
    is_active = models.BooleanField(default=False) 

    def __str__(self) -> str:
        return f"{self.name}  - {self.username} - {self.password}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

