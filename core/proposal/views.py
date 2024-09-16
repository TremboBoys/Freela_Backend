from rest_framework.viewsets import ModelViewSet
from core.proposal.serializer import ProposalSerializer, LanguageSerializer
from core.proposal.models import Proposal, Language
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from rest_framework.response import Response

class ProposalView(ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialzer = self.get_serializer(queryset, many=True)
        print()
        return Response(serialzer.data)
        

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