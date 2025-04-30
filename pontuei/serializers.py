from rest_framework import serializers

from pontuei.models import Sala, Jogador, HistoricoPontuacao


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'


class HistoricoPontuacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoPontuacao
        fields = '__all__'
