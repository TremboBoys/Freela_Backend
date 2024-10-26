from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from core.project.serializer import ProjectSerializer
from core.project.models import Project
from core.proposal.models import AcceptProposal
from rest_framework.response import Response
from rest_framework import status
class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class FinishedProjectAPIView(APIView):
    def patch(self, request):
        id_project = request.data['id']
        print(id_project)
        
        if not id_project:
            return Response({"message": "O id do projeto é necessário!"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            project = Project.objects.get(pk=id_project)
            print(project.status)
        except Project.DoesNotExist:
            return Response({"message": "O projeto não existe!"}, status=status.HTTP_404_NOT_FOUND)
        
        if project.status == 2:
            project.status= 3
            project.save()
        elif project.status == 3:
            return Response({"message": "O projeto já está finalizado"}, status=status.HTTP_409_CONFLICT)
        elif project.status == 1:
            return Response({"message": "Para que um projeto sejá finalizado, é necessário aceitar uma proposta para este"}, status=status.HTTP_409_CONFLICT)
        return Response({"message": "Parabéns, o projeto foi finalizado!"}, status=status.HTTP_201_CREATED)
    


            

