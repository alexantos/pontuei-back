from rest_framework import serializers

from pontuei.models import Sala, Jogador


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'
