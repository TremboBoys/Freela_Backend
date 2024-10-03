from passageidentity import Passage
from config import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

app_id = settings.PASSAGE_APP_ID
app_key = settings.PASSAGE_API_KEY

passage = Passage(api_key=app_key, app_id=app_id)

def authenticate_user(token):
    try:
        user_id = passage.authenticate_request(token)
        return user_id
    except Exception as error: 
        return None

class LoginAPIView(APIView):
    def post(self, request):
        token = request.data.get('token')

        if not token:
            return Response({"message": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if authenticate_user(token=token):
            return Response({"message": "Logged"})
        else:
            return Response({"message": "Not allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
