from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from utils.mixins.create_ai_mixin import CreateAiModelMixin

class ModelAiViewSet(CreateAiModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     GenericViewSet):
    pass