# Generated by Django 5.1.2 on 2024-10-08 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baralho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('frente', models.CharField(max_length=200)),
                ('resposta', models.TextField()),
                ('dificuldade', models.CharField(choices=[('facil', 'Fácil'), ('medio', 'Médio'), ('dificil', 'Difícil'), ('impossivel', 'Impossível')], default='facil', max_length=20)),
                ('baralho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='accounts.baralho')),
            ],
        ),
    ]
