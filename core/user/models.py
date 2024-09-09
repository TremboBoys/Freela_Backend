from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    password= models.CharField(max_length=45)
    code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}  - {self.username} - {self.password}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

class EmailVerification(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

class ForgetPassword(models.Model):
    email = models.EmailField(max_length=45)
    token = models.CharField(max_length=45)

    def __str__(self):
        return self.token
