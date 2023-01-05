from rest_framework import routers
from .api import AlumnosViewSet, PersonalViewSet, PeriodosEscolaresViewSet, CarrerasViewSet

router =  routers.DefaultRouter()

router.register('api/Alumnos', AlumnosViewSet, 'Alumnos')
router.register('api/Personal', PersonalViewSet, 'Personal')
router.register('api/Carreras', CarrerasViewSet, 'Carreras')
router.register('api/PeriodosEscolares', PeriodosEscolaresViewSet, 'PeriodosEscolares')


urlpatterns = router.urls 