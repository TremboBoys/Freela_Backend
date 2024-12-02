from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.user.use_case.authenticate import authenticate
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not authenticate(email):
            return Response({"message": "User not authenticated!"}, status=status.HTTP_410_GONE)
        else:
            return Response({"message": "User authenticated!"}, status=status.HTTP_200_OK)
            
    
