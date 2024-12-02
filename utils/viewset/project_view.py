from rest_framework import mixins
from utils.mixins.create_project import CreateServiceModelMixin
from rest_framework.viewsets import GenericViewSet

class ProjectModelViewSet(
                        CreateServiceModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet
                        ):
    pass