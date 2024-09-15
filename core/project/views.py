from rest_framework.viewsets import ModelViewSet
from core.project.serializer import ProjectSerializer
from core.project.models import Project

class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer