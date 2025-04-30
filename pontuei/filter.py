from django_filters import FilterSet

from pontuei.models import Jogador, Sala, HistoricoPontuacao


class JogadorFilter(FilterSet):
    class Meta:
        model = Jogador
        fields = {
            'sala': ['exact'],
        }

class SalaFilter(FilterSet):
    class Meta:
        model = Sala
        fields = {
            'codigo': ['exact'],
        }

class HistoricoPontuacaoFilter(FilterSet):
    class Meta:
        model = HistoricoPontuacao
        fields = {
            'jogador': ['exact'],
        }