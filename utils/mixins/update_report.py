from rest_framework.response import Response
from core.project.models import Project
from core.perfil.models import MyProjects, Perfil
from rest_framework import status
#from core.pay.use_case.pix import create_transacation
import requests
class UpdateReportModelMixin:
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        accept = serializer.validated_data.get('accept_proposal')
        is_accept = serializer.validated_data.get('is_accept')

        if is_accept == True:
            project = accept.proposal.project
            project.status = 3
            project.save()

            try:
                my_project = MyProjects.objects.get(project=project.pk)
                
                if my_project.in_execution == True:
                    data = {
                        'in_execution': False
                    }
                    try:
                        response = requests.patch(f"http://127.0.0.1:8000/api/perfil/myProjects/{my_project.pk}/", json=data)
                    except Exception as error:
                        return Response({"message": f"There's a error in request project: {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    
                    print(response)
                    print(response.json())
                    print(response.status_code)
                    if response.status_code != 200:
                        return Response({"message": f"There is a error in my_project api"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    print("The project was finished!")
            except MyProjects.DoesNotExist as error:
                return Response({"message": f"Oh, are you a hacker? {error}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
