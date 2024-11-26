from core.service.models import ContractService
from core.service.serializer import ContractServiceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.perfil.models import Perfil
from core.pay.models import Address
from core.pay.use_case.pix import create_transaction
class ContractServiceAPIView(APIView):
    def post(self, request):
        objeto = request.data.get('objeto')
        if not objeto:
            return Response({"message": "objeto is required"})
        try:
            transaction = create_transaction(objeto=objeto)
        except ValueError as err:
            return Response({'message': err})
        
        return Response({"message": transaction}, status=status.HTTP_201_CREATED)
        
                
