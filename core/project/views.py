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
from core.pay.use_case.pix import create_transaction_with_project
class ProjectView(ProjectModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    

class FineshedProjectAPIView(APIView):
    def patch(self, request):
        id_project = request.query_params.get('id') 
        cpf = request.data.get('cpf')
        email = request.data.get('freelancer_email')
        
        if not id_project:
            return Response({"message": "id project is required"}, status=status.HTTP_404_NOT_FOUND)
        if not cpf or not email:
            return Response({'message': "Cpf and email is required"}, status=status.HTTP_404_NOT_FOUND)
        
        user = Address.objects.filter(address__perfil__user__email=email).first()
        
        if not user:
            return Response({'message': "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        report = Report.objects.filter(accept_proposal__proposal__project__pk=id_project).last()
        
        if not report:
            return Response({"message": "Doesn't have a report for this project"}, status=status.HTTP_404_NOT_FOUND)
        
        report.is_accept = True
        report.save()
        
        try:
            transaction = create_transaction_with_project(amount=report.accept_proposal.proposal.price, email_payer=user.perfil.user.email, type_data="cpf", number=cpf, method="pix", accept_proposal=report.accept_proposal)
        except ValueError as err:
            return Response({"message": f"There is a error in create_transaction"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"message": transaction}, status=status.HTTP_200_OK)
        
            



        
            

