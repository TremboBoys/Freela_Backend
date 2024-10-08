from rest_framework.serializers import ModelSerializer
from core.service.models import ContractService
class ContractServiceSerializer(ModelSerializer):
    class Meta:
        model = ContractService
        fields = "__all__"