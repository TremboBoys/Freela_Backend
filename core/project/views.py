from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from core.project.serializer import ProjectSerializer
from core.project.models import Project
from core.proposal.models import AcceptProposal
from rest_framework.response import Response
from rest_framework import status
from utils.viewset.project_view import ProjectModelViewSet
from core.report.models import Report
from core.pay.models import Address
from core.pay.use_case.pix import create_transaction
from core.report.models import Report

class ProjectView(ProjectModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class FinishedProjectAPIView(APIView):
    def patch(self, request):
        objeto = request.query_params.get('objeto')
        if not objeto:
            return Response({"message": "The object is required"})
        report = Report.objects.filter(accept_proposal__proposal__project__pk=objeto['project_id']).last()
        if not report:
            return Response({"message": "There is a error in report"}, status=status.HTTP_404_NOT_FOUND)
        report.is_accept = True
        report.save()
        try:
            transaction = create_transaction(objeto=objeto)
        except ValueError as err:
            return Response({"message": err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        return Response({"message": transaction}, status=status.HTTP_200_OK)
    


        
            

