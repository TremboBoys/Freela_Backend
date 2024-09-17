from rest_framework.viewsets import ModelViewSet
from core.proposal.serializer import ProposalSerializer, LanguageSerializer
from core.proposal.models import Proposal, Language
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from rest_framework.response import Response
from core.project.models import Project
from rest_framework import status
from rest_framework.decorators import action

class ProposalView(ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def list(self, request, *args, **kwargs):
        email_contratante = request.query_params.get('email', None)

        if not email_contratante:
            return Response({"message:": "O email do contrante é necessário"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset().filter(
            project__contractor__email =email_contratante
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @receiver(post_save, sender=Proposal)
    def newProposal(sender, instance, created, **kwargs):
        if created:
            subject = "Seu projeto possui uma nova proposta"
            message = f"Olá, o usuário {instance.user.name} enviou uma proposta para você\nValor: R${instance.price}\nPrazo de entrega: {instance.delivery}"   
            recipient_list = [instance.project.contractor.email]
            from_email = "martinsbarroskaua85@gmail.com'"
            send_mail (
                subject=subject,
                message=message,
                recipient_list=recipient_list,
                from_email=from_email,
            )

class LanguageView(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

