# Generated by Django 5.2 on 2025-04-26 06:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=127)),
                ('pontuacao', models.PositiveIntegerField()),
                ('cor', models.CharField(max_length=7)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pontuei.sala')),
            ],
        ),
    ]
