from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from core.user.models import User
from core.user.permissions import freelancer_group, contratante
from core.user.use_case.validation import validate

class UserAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user_type = request.data.get('type')
        
        if not validate(name=name, user_type=user_type, username=username, email=email, password=password):
            return Response({"message": "Error in validated data"}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({"message": "User already exists"}, status=status.HTTP_409_CONFLICT)
        
        try:
            if user_type == "contractor":
                user_type_value = 2
                user_group = contratante
            elif user_type == "freelancer":
                user_type_value = 3
                user_group = freelancer_group
            else:
                return Response({"message": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(
                email=email, 
                password=password,
                name=name, 
                username=username, 
                type_user=user_type_value
            )            
            user.groups.add(user_group)
            user.save()

            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            print(error)
            return Response({"message": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
