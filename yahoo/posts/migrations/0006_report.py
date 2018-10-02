# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-22 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20180531_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Qual o seu e-mail?', max_length=200)),
                ('Seu_nome', models.CharField(help_text='Qual o seu nome?', max_length=200)),
                ('Crescimento', models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], help_text='Sua empresa esta crescendo neste ano?', max_length=12)),
                ('Segmento', models.CharField(choices=[('Serviço', 'Serviço'), ('Indústria', 'Indústria'), ('Agrobusiness', 'Agrobusiness'), ('Varejo', 'Varejo'), ('Financeiro', 'Financeiro'), ('Consultoria', 'Consultoria'), ('Tecnologia', 'Tecnologia')], help_text='Sua empresa esta crescendo neste ano?', max_length=12)),
                ('Competitor', models.CharField(help_text='Nome de um concorrente direto ou produto substituto', max_length=12)),
            ],
            managers=[
                ('pdobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
