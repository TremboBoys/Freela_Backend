from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.pay.models import City, Address
from core.perfil.models import Perfil
from core.user.models import User

class CityAPIView(APIView):
    def post(self, request):
        city = request.data.get('city')
        country = request.data.get('country')
        state = request.data.get('state')
        code = request.data.get('code')
        
        if not city or not country or not code:
            return Response({"message": "Country or city is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            City.objects.create(city=city, country=country, state=state, zip_code=code)
        except Exception as error:
            return Response({"message": "Error in create city"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"message": "Created new city!"}, status=status.HTTP_201_CREATED)
        
    
    def get_queryset(self):
        return City.objects.all()
        
    def get(self, request):
        queryset = self.get_queryset()
        cities = [{
            "id": city.id,
            "country": city.country,
            "state": city.state,
            "city": city.city,
            "zip_code": city.zip_code
        } for city in queryset] 
        
        return Response(cities, status=status.HTTP_200_OK)  
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AddressAPIView(APIView):
    def post(self, request):
        required_fields = {
            "email": request.data.get('email'),
            "phone": request.data.get('phone'),
            "street_name": request.data.get('street'),
            "street_number": request.data.get('number'),
            "complement": request.data.get('complement'),
            "neighborhood_name": request.data.get('neighborhood'),
            "zip_code": request.data.get('zip_code'),
        }

        missing_fields = [key for key, value in required_fields.items() if not value]
        if missing_fields:
            return Response(
                {"message": f"Missing fields: {', '.join(missing_fields)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(email=required_fields["email"]).first()
        if not user:
            return Response(
                {"message": "User with the provided email not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        perfil = Perfil.objects.filter(user=user).first()
        if not perfil:
            return Response(
                {"message": "Profile for the given user not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        city = City.objects.filter(zip_code=required_fields["zip_code"]).first()
        if not city:
            return Response(
                {"message": "Invalid zip code. City not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        Address.objects.create(
            city=city,
            perfil=perfil,
            neighborhood_name=required_fields["neighborhood_name"],
            street_name=required_fields["street_name"],
            street_number=required_fields["street_number"],
            phone=required_fields["phone"],
            complement=required_fields["complement"]
        )

        return Response({"message": "Address created successfully!"}, status=status.HTTP_201_CREATED)

        
        
        
        
        
            
    
            
            