from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.user.models import 
from django.contrib.auth.models import Group

admin_group = Group.objects.get(name='admin')
print('o')
freelancer_group = Group.objects.get(name="freelancers")
print('p')
contratante = Group.objects.get(name="contractors")
print('q')





