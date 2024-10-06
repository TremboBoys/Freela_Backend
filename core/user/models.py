from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser, BaseUserManager, Group, Permission
class User(AbstractUser):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=45, unique=True)
    password= models.CharField(max_length=45)
    code = models.CharField(max_length=6, blank=True, null=True)
    class TypeUser(models.IntegerChoices):
        ADMIN = 1, "Admin"
        CONTRACTORS = 2, "Contractors"
        FREELANCERS = 3, "Freelancers"
    type_user = models.IntegerField(("Type of user"), choices=TypeUser.choices, default=TypeUser.FREELANCERS, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}  - {self.username} - {self.password}"
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Change this to a unique name
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Change this to a unique name
        blank=True,
    ) 

    USERNAME_FIELD = 'username'  # Campo que será usado para autenticação
    REQUIRED_FIELDS = ['email']  # Campos obrigatórios ao criar superusuário

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

class EmailVerification(models.Model):
    email = models.EmailField(unique=False)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

class ForgetPassword(models.Model):
    email = models.EmailField(max_length=45)
    token = models.CharField(max_length=45)

    def __str__(self):
        return self.token
