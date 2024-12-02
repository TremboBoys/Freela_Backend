from rest_framework.response import Response
from rest_framework import status
from core.report.models import Report
from core.proposal.models import AcceptProposal

class CreateReportModelModelMixin:
    def create(self, request, *args, **kwargs):
        is_accept = request.data.get('is_accept', False)
        accept_proposal = request.data.get('accept_proposal')
        title = request.data.get('title')
        text = request.data.get('text_body')
        
        try:
            proposal = AcceptProposal.objects.get(pk=accept_proposal)
        except AcceptProposal.DoesNotExist:
            return Response({"message": "Proposal Doens't exists"}, status=status.HTTP_404_NOT_FOUND)
    
        if not accept_proposal or not title or not text:
            return Response({"message": "is_accept or accept_proposal is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        existing_report = Report.objects.filter(accept_proposal=proposal).first() 
        if existing_report and existing_report.is_accept:
            return Response({"message": "Report for this project is accept"}, status=status.HTTP_412_PRECONDITION_FAILED)

        try:
           report = Report.objects.create(is_accept=is_accept, accept_proposal=proposal, title=title, text_body=text)
        except Exception as error:
            return Response({"message": f"Has a error in create report: {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({
            "message": "Report created", 
            "data": {
                "id": report.pk,
                "is_accept": report.is_accept,
                "accept_proposal": report.accept_proposal.pk,
            }
        }, status=status.HTTP_201_CREATED)
    
        
            
    
    



