from django.contrib.auth.models import Group
from rest_framework.views import APIView

free_group = Group.objects.get('group')
month_group = Group.objects.get('month')
year_group = Group.objects.get('year')



