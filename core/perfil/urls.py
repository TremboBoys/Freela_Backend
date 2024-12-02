from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.perfil.views import PerfilView, PerfilCurrentUserView, ProView, AreaView, SubAreaView, HabilityView, MyProjectsView, NacionalityView, MyCompetencyView, ChoiceProjectView, PerfilUpdateCollectIdAPIView

router = DefaultRouter()
router.register(r"perfil", PerfilView, basename="perfil")
router.register(r"currentUser", PerfilCurrentUserView, basename="currentUser")
router.register(r"pro", ProView, basename="Pro")
router.register(r"area", AreaView, basename="area")
router.register(r"subArea", SubAreaView, basename="subArea")
router.register(r"hability", HabilityView, basename="habiliity")
router.register(r"myProjects", MyProjectsView, basename="myProjects")
router.register(r"nacionality", NacionalityView, basename="nacionality")
router.register(r"myCompetence", MyCompetencyView, basename="myCompetency")
router.register(r"choiceProject", ChoiceProjectView, basename="choiceProject")


urlpatterns = [
    path("", include(router.urls)),
    path("perfil_mercado/", PerfilUpdateCollectIdAPIView.as_view(), name="perfil_mercado_pago")
]