from django_filters import FilterSet

from pontuei.models import Jogador, Sala


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