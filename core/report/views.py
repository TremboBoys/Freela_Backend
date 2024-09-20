from rest_framework.viewsets import ModelViewSet
from core.report.models import Report
from core.report.serializer import ReportSerializer
from django.dispatch import receiver
from django.db.models.signals import post_save
class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    #@receiver(post_save, sender=Report)
    #def dla():
        #print("Erro na api")

    
