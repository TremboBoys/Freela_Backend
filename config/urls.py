from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/perfil/', include('core.perfil.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('api/user/', include('core.user.urls')),
    path('api/project/', include('core.project.urls')),
    path('api/media/', include('uploader.router')),
    path('api/proposal/', include('core.proposal.urls')),
    path('api/report/', include('core.report.urls')),
    path('api/service/', include('core.service.urls')),
    path('api/ads/', include('core.ads.urls')),
    path("api/pay/", include("core.pay.urls")),
]
