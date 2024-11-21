from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.pay.models import City, Address
from core.perfil.models import Perfil
from core.user.models import User
from core.pay.use_case.pix import create_address, get_address, update_address
from rest_framework.viewsets import ModelViewSet
from core.pay.serializer import CitySerializer


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
        

    
        
    
        
        
        
        

    
    



        
            
    
            
            