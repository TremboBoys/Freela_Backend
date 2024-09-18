from rest_framework.viewsets import ModelViewSet, AcceptPurposeViewSet, PurposeViewSet
from core.proposal.serializer import ProposalSerializer, LanguageSerializer, AcceptProposalSerializer
from core.proposal.models import Proposal, Language, AcceptProposal
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from rest_framework.response import Response
from core.project.models import Project
from rest_framework import status
from rest_framework.decorators import action
from core.perfil.models import MyProjects
class ProposalView(PurposeViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        project = serializer.validated_data.get('project')

        if project.in_execution == True:
            Response({"message": "Esse projeto não aceita mais propostas"}, status=status.HTTP_423_LOCKED)

        return super().create(request, *args, **kwargs)

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
            message = f"Olá, o usuário {instance.perfil.user.name} enviou uma proposta para você\nValor: R${instance.price}\nPrazo de entrega: {instance.delivery}"   
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

class AcceptProposalView(AcceptPurposeViewSet):
    queryset = AcceptProposal.objects.all()
    serializer_class = AcceptProposalSerializer

    @receiver(pre_save, sender=AcceptProposal)
    def updateStatusProject(instance, sender, **kwargs):
        newProjects = MyProjects.objects.create(perfil=instance.proposal.perfil, project=instance.proposal.project, in_execution=True)
        newProjects.save()
        Project.objects.filter(id=instance.proposal.project.pk).update(in_execution=True)
    
    @receiver(post_save, sender=AcceptProposal)
    def acceptPurpose(instance, created, *args, **kwargs):
        if created:
            subject = f"Sua proposta foi aceita!"
            message = f"Olá {instance.proposal.perfil.user.email}, sua proposta para o projeto para o projeto: {instance.proposal.project.title} foi aceita!!!!!!"
            recipient_list = [instance.proposal.project.contractor.email]
            from_email = "martinsbarroskaua85@gmail.com"
            send_mail(
                 recipient_list=recipient_list,
                message=message,
                subject=subject, 
                from_email=from_email
            )
                    


