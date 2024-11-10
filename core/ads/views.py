from rest_framework.viewsets import ModelViewSet
from core.ads.models import Ads, AdsCategory
from core.ads.serializer import AdsSerializer, AdsCategorySerializer
from utils.viewset.create_ai_view import ModelAiViewSet
class AdsViewSet(ModelAiViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class AdsCategoryViewSet(ModelViewSet):
    queryset = AdsCategory.objects.all()
    serializer_class = AdsCategorySerializer

