from rest_framework.serializers import ModelSerializer
from core.ads.models import Ads, AdsCategory

class AdsSerializer(ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"

class AdsCategorySerializer(ModelSerializer):
    class Meta:
        model = AdsCategory
        fields = "__all__"