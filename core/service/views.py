from core.service.models import ContractService
from core.service.serializer import ContractServiceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.perfil.models import Perfil
from core.pay.models import Address
#from core.pay.use_case.pix import create_transaction_with_service
from core.pay.models import Transaction
class ContractServiceAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        type_service = request.data.get('service')
        
        if not email or not type_service:
            return Response({"message": "Email and type_serivce is required"}, status=status.HTTP_400_BAD_REQUEST)
        user = Address.objects.filter(perfil__user__email=email).first()
        if not user:
            return Response({'message': "User not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        if type_service == "Month":
            type_service = 2
            new_service = ContractService.objects.create(type_service=type_service, contractor=user.perfil)
            new_service.save()
            #try:
            #    new_transaction = create_transaction_with_service(email_payer=user.perfil.user.email, amount=30.00, service=new_service, cpf=user.cpf, type_data='cpf', method="pix")
            #except ValueError as err:
            #    return Response({'message': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
