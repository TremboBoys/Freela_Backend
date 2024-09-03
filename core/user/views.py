
from rest_framework.views import APIView

class UserAPIView(APIView):
    def post(self, request):
        data = request.data
        email = data['email']
        password = data['password']
        code = data['code']
        