from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from core.user.models import User, EmailVerification
#from core.user.permissions import freelancer_group, contratante
from core.user.use_case.validation import validate
from core.user.serializer import UserSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random


class SendCode(APIView):
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response({"message": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        code = random.randint(100000, 999999)
        
        EmailVerification.objects.create(email=email, code=code)
        
        html_message = render_to_string('code_user.html', {'code': code})
        text_content = strip_tags(html_message)
        
        subject = 'Your code!'
        from_email = "martinsbarroskaua85@gmail.com"
        
        email_message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=[email])
        email_message.attach_alternative(html_message, "text/html")
         
        try:
            email_message.send()
        except Exception as error:
            return Response({"message": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"message": "Code sent to your email!"}, status=status.HTTP_201_CREATED)

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
            elif user_type == "freelancer":
                user_type_value = 3
            else:
                return Response({"message": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(
                email=email, 
                password=password,
                name=name, 
                username=username, 
                type_user = user_type_value
            )   
            user.groups.add(user_type_value)            
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except Exception as error:
            print(error)
            return Response({"message": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_queryset(self):
        return User.objects.all()
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request):
        code = request.data.get('code')
        update_type = request.data.get('update')
        
        try:
            code_exists = EmailVerification.objects.get(code=code)
        except EmailVerification.DoesNotExist as error:
            return Response({"message": "Token hasn't exists"}, status=status.HTTP_404_NOT_FOUND)
        
        email = code_exists.email
        code_exists.delete()
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "User doesn't exists"}, status=status.HTTP_404_NOT_FOUND)

        
        
        if update_type == 'password':
            password = request.data.get('password')
            try:
                user.set_password(password)
                user.save()
            except User.DoesNotExist:
                return Response({"message": "User doesn't exists"}, status=status.HTTP_404_NOT_FOUND)
            message = "updated password!"
            
        elif update_type == "user_type":
            user_type = request.data.get('type')
            if user_type == "admin":
               return Response({"message": "Not authorized!"}, status=status.HTTP_423_LOCKED)
            try:
                if user_type == "freelancer":
                    user.type_user = 3
                    user.groups.remove(contratante)
                    user.groups.add(freelancer_group)
                else:
                    user.type_user == 2
                    user.groups.remove(freelancer_group)
                    user.groups.add(contratante)
            except Exception as error:
                return Response({"message": f"Error update user: {str(error)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            message = "Updated user type!"
        elif update_type == "email":
            newEmail = request.data.get('email')
            
            if not newEmail:
                return Response({"message": "Email is required!"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                user.email = newEmail
                user.save()
            except Exception as error:
                return Response({"message": f"Error in update email!: {str(error)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            message = "Updated email!"

        return Response({"message": message}, status=status.HTTP_200_OK)
    

            
            
                
                    
            