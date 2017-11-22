# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171122_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ra', models.IntegerField(unique=True, verbose_name='RA')),
                ('password', models.CharField(max_length=200, verbose_name='Senha')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=50, verbose_name='E-Mail')),
                ('perfil', models.CharField(max_length=1, verbose_name='Perfil')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
