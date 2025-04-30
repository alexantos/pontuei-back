from django.urls import include, path
from rest_framework import routers

from pontuei.views import SalaViewSet, JogadorViewSet, HistoricoPontuacaoViewSet

router = routers.DefaultRouter()
router.register(r'salas', SalaViewSet)
router.register(r'jogadores', JogadorViewSet)
router.register(r'historico-pontuacao', HistoricoPontuacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
