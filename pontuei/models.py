import uuid

from django.db import models


class Sala(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=31)

    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)


class Jogador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=127)
    pontuacao = models.PositiveIntegerField()
    cor = models.CharField(max_length=31)
    sala = models.ForeignKey(to=Sala, on_delete=models.CASCADE)

    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)


class HistoricoPontuacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pontuacao = models.PositiveIntegerField()
    jogador = models.ForeignKey(to=Jogador, on_delete=models.CASCADE)

    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)