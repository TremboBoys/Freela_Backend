from django.contrib import admin
from core.project.models import Project, ProjectIntegration, IntegrationType
# Register your models here.


admin.site.register(Project)
admin.site.register(ProjectIntegration)
admin.site.register(IntegrationType)