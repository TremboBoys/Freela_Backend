from rest_framework.response import Response
from core.project.models import Project

class UpdateReportModelMixin:
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(serializer)
        accept = serializer.validated_data.get('accept_proposal')
        print(accept)
        is_accept = serializer.validated_data.get('is_accept')
        print(is_accept)

        if is_accept == True:
            project = accept.proposal.project
            project.status = 3
            project.save()
            
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
