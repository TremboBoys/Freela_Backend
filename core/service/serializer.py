from rest_framework.serializers import ModelSerializer
from core.service.models import Service
class ServiveSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"