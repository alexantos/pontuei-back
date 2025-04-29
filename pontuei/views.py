from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from pontuei.filter import JogadorFilter, SalaFilter
from pontuei.models import Sala, Jogador
from pontuei.serializers import SalaSerializer, JogadorSerializer


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
