from core.report.models import Report
from core.report.serializer import ReportSerializer
from utils.viewset.report_view import ReportViewSet
from core.report.use_case.ai_translate import TranslationService
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
class ReportViewSet(ReportViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
            


class TranslationAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.translation_service = TranslationService()

    def post(self, request):
        text = request.data.get('text', None)
        if not text:
            return Response({"error": "Text is required"}, status=status.HTTP_400_BAD_REQUEST)

        translated_text = self.translation_service.translate(text)
        return Response({"translated_text": translated_text}, status=status.HTTP_200_OK)


    



    
