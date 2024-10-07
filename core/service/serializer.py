from rest_framework.serializers import ModelSerializer
from core.service.models import Service, ContractService
class ServiveSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class ContractServiceSerializer(ModelSerializer):
    class Meta:
        model = ContractService
        fields = "__all__"