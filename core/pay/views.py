from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.pay.models import City, Address, Transaction
from core.pay.use_case.pix import create_address, get_address, update_address
from rest_framework.viewsets import ModelViewSet
from core.pay.serializer import CitySerializer
from core.service.models import ContractService
from core.perfil.models import MyProjects, Perfil
import requests
from core.pay.use_case.pix import urlpix
from core.proposal.models import AcceptProposal
from core.ads.models import Ads
print(urlpix)
class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
class AddressAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        street = request.data.get('street')
        street_number = request.data.get('number')
        complement = request.data.get('complement')
        zip_code = request.data.get('zip_code')
        neighborhood_name = request.data.get('neighborhood')
        
        if not email or not phone or not street or not street_number or not complement or not zip_code:
            return Response({"message": "Insufficient data"}, status=status.HTTP_400_BAD_REQUEST)
        
        perfil = Perfil.objects.filter(user__email=email).first()
        if not perfil:        
            return Response({"message": "Perfil Doesn't exists"}, status=status.HTTP_404_NOT_FOUND)
        
        city = City.objects.filter(zip_code=zip_code).first()
        if not city:
            return Response({"message": "City Doens't exists"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            Address.objects.create(perfil=perfil, city=city)
        except BaseException as error:
            return Response({"message": f"Error in create address"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if not create_address(email_payer=perfil.user.email, name_payer=perfil.user.name, street_name=street, street_number=street_number, complement_address=complement, cellphone_number=phone, neighborhood_name=neighborhood_name, zip_code=city.zip_code, city_name=city.city  ):
            return Response({"message": "Cannot created address in address ms"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"message": "Address created with successfully!"},status=status.HTTP_201_CREATED)

    def get(self, request):
        email = request.query_params.get('email')
        perfil = Address.objects.filter(perfil__user__email=email).first()
        
        if not perfil:
            return Response({"message": "email doesn't exists"}, status=status.HTTP_404_NOT_FOUND)      
        
        address = get_address(email=perfil.perfil.user.email)
        
        return Response({"message": address}, status=status.HTTP_200_OK)
    
    def put(self, request):
        id_address = request.data.get('id_address')
        old_email = request.query_params.get('email')
        new_email = request.data.get('new_email')
        street_name = request.data.get('street_name')
        street_number = request.data.get('street_number')
        complement = request.data.get('complement_address') 
        phone = request.data.get('cellphone_number')
        neighborhood_name = request.data.get('neighborhood_name')
        city = request.data.get('city_name')
        name = request.data.get('name_payer')
        zip_code = request.data.get('zip_code') 
        
        if not id_address or not old_email or not new_email or not street_name or not complement or not phone or not neighborhood_name or not city or not name or not zip_code or not street_number:
            return Response({"message": "Datas required not offering"}, status=status.HTTP_400_BAD_REQUEST)

        address = Address.objects.filter(perfil__user__email=old_email).first()
        
        if not address:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        address.city.city = city
        address.city.zip_code = zip_code
        address.perfil.user.email = new_email        
        address.save()
        
        success = update_address(
            id_address=id_address,
            street_name=street_name,
            street_number=street_number,
            complement_address=complement,
            cellphone_number=phone,
            neighborhood_name=neighborhood_name,
            city_name=city,
            name_payer=name,
            email_payer=new_email,
            zip_code=zip_code
        )

        if not success:
            return Response({"message": "Failed to update external service"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": f"Address updated successfully: {success}"}, status=status.HTTP_200_OK)        
        

class TransactionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        
        payer_email = data.get('payer', {}).get('email')
        if not payer_email:
            return Response({"error": "O campo 'email_payer' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = Address.objects.filter(perfil__user__email=payer_email).first()
            if not user:
                return Response({"error": "Usuário não encontrado com o email fornecido."}, status=status.HTTP_404_NOT_FOUND)
            
            if 'project_id' in data:
                project = AcceptProposal.objects.filter(proposal__pk=data['project_id']).first()
                if not project:
                    return Response({"error": "Proposta não encontrada para o projeto fornecido."}, status=status.HTTP_404_NOT_FOUND)
                
                response = self.create_pix_transaction(data, user.perfil.access_token_mercado_pago)
                transaction = Transaction.objects.create(
                    id_transaction=response['id_transaction'],
                    user=user.perfil,
                    accept_proposal=project,
                    amount=data['transaction_amount'],
                    method=data['payment_method_id'],
                    number=data.get('number')
                )
                return Response(self.prepare_response(data, response), status=status.HTTP_201_CREATED)
            
            elif 'service_id' in data:
                service_type = data['service_id']
                service = ContractService.objects.create(type_of_service=service_type, contractor=user.perfil)
                response = self.create_pix_transaction(data)
                transaction = Transaction.objects.create(
                    id_transaction=response['id_transaction'],
                    user=user.perfil,
                    service=service,
                    amount=data['transaction_amount'],
                    method=data['payment_method_id'],
                    number=data.get('number')
                )
                return Response(self.prepare_response(data, response), status=status.HTTP_201_CREATED)
            
            elif 'ads_id' in data:
                ads = Ads.objects.filter(pk=data['ads_id']).first()
                if not ads:
                    return Response({"error": "Anúncio não encontrado para o ID fornecido."}, status=status.HTTP_404_NOT_FOUND)
                
                response = self.create_pix_transaction(data)
                transaction = Transaction.objects.create(
                    id_transaction=response['id_transaction'],
                    user=user.perfil,
                    ads=ads,
                    amount=data['transaction_amount'],
                    method=data['payment_method_id'],
                    number=data.get('number')
                )
                return Response(self.prepare_response(data, response), status=status.HTTP_201_CREATED)
            
            else:
                return Response({"error": "Nenhum identificador válido (project_id, service_id ou ads_id) foi fornecido."}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": f"Ocorreu um erro: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        id_transaction = request.query_params.get('id_transaction')
        status_approved = request.data.get('status')
        status_accredited = request.data.get('status_accredited')
        
        if not id_transaction or not status_approved or not status_accredited:
            return Response({"message": "Você não me forneceu todos os dados necessários."}, status=status.HTTP_400_BAD_REQUEST)
        
        transaction = Transaction.objects.filter(id_transaction=id_transaction).first()
        if not transaction:
            return Response({"message": "A transação não procede."}, status=status.HTTP_404_NOT_FOUND)
         
        if status_approved == "approved" or status_accredited == "accredited":   
            if transaction.accept_proposal is not None:
                transaction.is_paid = True
                transaction.accept_proposal.proposal.project.status = 3
                transaction.accept_proposal.proposal.perfil.balance += transaction.amount
                my_projects = MyProjects.objects.get(project=transaction.accept_proposal.proposal.project)
                my_projects.in_execution = False
                my_projects.save()
                transaction.accept_proposal.proposal.project.save()
                transaction.accept_proposal.proposal.perfil.save()
                
            elif transaction.service is not None:
                transaction.is_paid = True
                transaction.service.is_paid = True
                transaction.user.is_pro = True
                transaction.service.save()
                transaction.user.save()
            elif transaction.ads is not None:
                transaction.is_paid = True
                transaction.ads.is_paid = True
                transaction.ads.save()
                
            transaction.save()
            return Response({"message": "Pagamento salvo com sucesso."}, status=status.HTTP_200_OK)

    def create_pix_transaction(self, data):
        print("Estou sendo chamado!")
        try:
            payer_data = data.get('payer', {})
            access_token = data.get('token')
            
            if not access_token:
                raise ValueError("O 'access_token' é obrigatório.")
            
            if not payer_data.get('email') or not payer_data.get('identification', {}).get('type') or not payer_data.get('identification', {}).get('number'):
                raise ValueError("Dados incompletos do 'payer': 'email', 'type' e 'number' são obrigatórios.")
            
            request_json = {
                "transaction_amount": data.get('transaction_amount'),
                "payment_method_id": data.get('payment_method_id'),
                "payer": {
                    "email": payer_data['email'],
                    "identification": {
                        "type": payer_data['identification']['type'],
                        "number": payer_data['identification']['number']
                    }
                },
                "access_token": access_token
            }
            print("JSON para requisição:", request_json)
            
            response = requests.post(f"{urlpix}/transaction", json=request_json)
            print(response)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ValueError(f"Erro na requisição ao PIX: {str(e)}")
        except ValueError as e:
            raise ValueError(f"Erro de validação: {str(e)}")
        except Exception as e:
            raise ValueError(f"Erro inesperado: {str(e)}")

    
    def prepare_response(self, data, response):
        if data['payment_method_id'] == "pix":
            return {
                "qr_code_base64": response.get('qr_code_base64'),
                "pix_copia_cola": response.get('pix_copia_cola')
            }
        return {"message": "Transação criada com sucesso."}
