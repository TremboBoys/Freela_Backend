from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.perfil.serializer import PerfilSerializer, PerfilCurrentUserSerializer, ProSerializer, MyCompetencySerializer, MyProjectSerializer, NacionalitySerializer, AreaSerializer,SubAreaSerializer, HabilitySerializer, ChoiceProjectSerializer
from .filters import PerfilFilter
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from core.perfil.models import Perfil, Pro, MyProjects, MyCompetency, Hability, Area, SubArea, Nacionality, ChoiceProject
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
from utils.viewset.potas_view import PotasViewSet
from rest_framework.views import APIView

class ChoiceProjectView(ModelViewSet):
    queryset = ChoiceProject.objects.all()
    serializer_class = ChoiceProjectSerializer

class PerfilView(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilUpdateCollectIdAPIView(APIView):
    def patch(self, request):
        # Obtendo parâmetros da requisição
        email = request.query_params.get('email')
        collector_id = request.data.get('collector_id')
        refresh_token = request.data.get("refresh_token")
        access_token = request.data.get('access_token')
        expiration_date_access_token = request.data.get('expiration_date_access_token')
        expiration_date_refresh_token = request.data.get('expiration_date_refresh_token')

        missing_fields = []
        if not email:
            missing_fields.append('email')
        if not collector_id:
            missing_fields.append('collector_id')
        if not refresh_token:
            missing_fields.append('refresh_token')
        if not access_token:
            missing_fields.append('access_token')
        if not expiration_date_access_token:
            missing_fields.append('expiration_date_access_token')
        if not expiration_date_refresh_token:
            missing_fields.append('expiration_date_refresh_token')

        if missing_fields:
            return Response(
                {"message": f"Campos obrigatórios ausentes: {', '.join(missing_fields)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        perfil = Perfil.objects.filter(user__email=email).first()
        if not perfil:
            return Response({'message': 'O email não procede'}, status=status.HTTP_404_NOT_FOUND)

        perfil.collector_id_mercado_pago = collector_id
        perfil.refresh_token_mercado_pago = refresh_token
        perfil.access_token_mercado_pago = access_token
        perfil.expiration_date_access_token_mercado_pago = expiration_date_access_token
        perfil.expiration_date_refresh_token_mercado_pago = expiration_date_refresh_token
        perfil.save()

        return Response({'message': "Perfil atualizado com sucesso"}, status=status.HTTP_200_OK)
    
class PerfilCurrentUserView(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilCurrentUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PerfilFilter
    
class ProView(ModelViewSet):
    queryset = Pro.objects.all()
    serializer_class = ProSerializer

class NacionalityView(ModelViewSet):
    queryset = Nacionality.objects.all()
    serializer_class = NacionalitySerializer

class AreaView(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class SubAreaView(ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer

class HabilityView(ModelViewSet):
    queryset = Hability.objects.all()
    serializer_class = HabilitySerializer

class MyProjectsView(PotasViewSet):
    queryset = MyProjects.objects.all()
    serializer_class = MyProjectSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        old_value = instance.in_execution
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        instance.refresh_from_db()
        new_value = instance.in_execution

        if old_value == True and new_value == False:
            print(instance.project.contractor.user)
            subject = f"O projeto {instance.project.title} está finalizado"
            message = f"Olá {instance.project.contractor.name}, seu projeto está finalizado"
            recipient_list = [instance.project.contractor.email]
            from_email = "martinsbarroskaua85@gmail.com"
            send_mail(
                message=message,
                subject=subject,
                recipient_list=recipient_list,
                from_email=from_email
            )
        
            return Response(serializer.data)
        elif old_value == False and new_value ==True:
            instance.refresh_from_db()
            return Response(serializer.data)

class MyCompetencyView(ModelViewSet):
    queryset = MyCompetency.objects.all()
    serializer_class = MyCompetencySerializer

    def list(self, request, *args, **kwargs):
        querset = self.queryset.order_by('-created_at')[:3]
        serializer = self.get_serializer(querset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

