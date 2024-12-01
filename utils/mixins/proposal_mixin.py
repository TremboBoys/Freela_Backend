from django.utils import timezone
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from core.perfil.models import MyProjects

class CreateProposalModelMixin:
    """
    Mixin to create a proposal instance, specifically for ProposalViewSet.
    """
    def create(self, request, *args, **kwargs):
        # Serialize the incoming data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        project = serializer.validated_data.get('project')
        perfil = serializer.validated_data.get('perfil')
        
        # Retrieve the current user's projects that are in execution
        my_projects = MyProjects.objects.filter(perfil=perfil, in_execution=True)
        number_projects = my_projects.count()
        
        # Convert 'created_at' to a datetime object (if it's a date) or ensure the comparison is correct
        project_creation_date = project.created_at if isinstance(project.created_at, datetime) else datetime.combine(project.created_at, datetime.min.time())

        # Ensure both project_creation_date and now() are naive or aware.
        if project_creation_date.tzinfo is None:  # If project is naive
            project_creation_date = timezone.make_aware(project_creation_date, timezone.get_current_timezone())
        
        # Get the current time as aware datetime
        current_time = timezone.now()

        # Calculate the difference in days
        days_since_creation = (current_time - project_creation_date).days
        
        # Validation for Pro users and project execution limits
        if not perfil.is_pro and days_since_creation <= 2:
            return Response(
                {"message": "Non-pro users cannot create a proposal within 2 days of project creation."},
                status=status.HTTP_423_LOCKED
            )
        
        if not perfil.is_pro and number_projects >= 2:
            return Response(
                {"message": "Non-pro users cannot have more than 2 active projects."},
                status=status.HTTP_423_LOCKED
            )
        
        if perfil.is_pro and number_projects >= 5:
            return Response(
                {"message": "Pro users cannot have more than 5 active projects."},
                status=status.HTTP_423_LOCKED
            )
        
        # Check if the project is already in execution
        if project.in_execution:
            return Response(
                {"message": "This project is already in execution!"},
                status=status.HTTP_423_LOCKED
            )

        # Perform the actual creation of the proposal
        self.perform_create(serializer)
        
        # Return the response with the created proposal
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """Save the serializer instance."""
        serializer.save()

    def get_success_headers(self, data):
        """Return headers for the successful creation of a resource."""
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
