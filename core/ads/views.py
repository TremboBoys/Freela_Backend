from rest_framework.viewsets import ModelViewSet
from utils.viewset.create_ai import AdsModelViewSet
from core.ads.models import Ads, AdsCategory
from core.ads.serializer import AdsSerializer, AdsCategorySerializer
class AdsViewSet(AdsModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class AdsCategoryViewSet(ModelViewSet):
    queryset = AdsCategory.objects.all()
    serializer_class = AdsCategorySerializer

