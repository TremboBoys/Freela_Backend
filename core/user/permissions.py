#Permissões de usuário
#Permissões por serviço
from rest_framework import permissions
from core.user.models import User
from core.service.models import Service

class CustomAccessPermission(permissions.BasePermission):
    
