from rest_framework.response import Response
from rest_framework import status
from core.report.models import Report
from core.pay.models import Transaction
from core.pay.use_case.pix import create_transaction
from core.project.models import Project
from core.perfil.models import Perfil
from core.proposal.models import Proposal, AcceptProposal

class FinishedProject_mixin:
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)      
        if getattr(instance, '_prefetched_objects_cache', None):
            
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)