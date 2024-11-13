from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import Group


admin_group = Group.objects.get_or_create(name='admin')

freelancer_group = Group.objects.get_or_create(name="freelancers")
contratante = Group.objects.get_or_create(name="contractors")





