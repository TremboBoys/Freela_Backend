from core.perfil.models import ChoiceProject, MyProjects
from core.perfil.serializer import MyProjectSerializer
from rest_framework.response import Response
from rest_framework import status
    
class SpeciafilyListModelMixin:
    """
    List speciafily model instance.
    """
    def list(self, request, *args, **kwargs):
        choiceObject = ChoiceProject.objects.values_list('project_id', flat=True)
        queryset = MyProjects.objects.filter(id__in=choiceObject)
        other = MyProjects.objects.exclude(id__in=choiceObject)
        in_execution = queryset.filter(in_execution=True)
        not_in_execution = queryset.filter(in_execution=False)

        other_serializer = MyProjectSerializer(other, many=True)
        in_execution_serializer = MyProjectSerializer(in_execution, many=True)
        not_in_execution_serializer = MyProjectSerializer(not_in_execution, many=True)
        
        return Response({'in_execution': f"{in_execution_serializer.data}", 'not_in_execution': f"{not_in_execution_serializer.data}", 'other': f"{other_serializer.data}"}, status=status.HTTP_200_OK)
