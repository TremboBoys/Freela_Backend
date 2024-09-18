from rest_framework.viewsets import ModelViewSet
from core.project.serializer import ProjectSerializer
from core.project.models import Project

from rest_framework.decorators import api_view
class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@api_view(['GET', 'POST', 'PUT'])
def finishedProject(self, request):
    pass