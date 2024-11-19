from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.pay.models import City

class CityAPIView(APIView):
    def post(self, request):
        city = request.data.get('city')
        country = request.data.get('country')
        state = request.data.get('state')
        
        if not city or not country:
            return Response({"message": "Country or city is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            City.objects.create(city=city, country=country, state=state)
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
            "city": city.city
        } for city in queryset] 
        
        return Response(cities, status=status.HTTP_200_OK)  
            
    
            
            