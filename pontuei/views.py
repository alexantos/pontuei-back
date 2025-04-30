from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from pontuei.filter import JogadorFilter, SalaFilter, HistoricoPontuacaoFilter
from pontuei.models import Sala, Jogador, HistoricoPontuacao
from pontuei.serializers import SalaSerializer, JogadorSerializer, HistoricoPontuacaoSerializer


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SalaFilter
    permission_classes = []


class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = JogadorFilter
    permission_classes = []


class HistoricoPontuacaoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoPontuacao.objects.all().order_by('criado')
    serializer_class = HistoricoPontuacaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricoPontuacaoFilter
    permission_classes = []
