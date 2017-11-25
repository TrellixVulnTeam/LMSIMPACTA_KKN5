# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Arquivoquestao(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idquestao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='IdQuestao')  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', unique=True, max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivoQuestao'


class Arquivoresposta(models.Model):
    idarquivoresposta = models.AutoField(db_column='IdArquivoResposta', primary_key=True)  # Field name made lowercase.
    idresposta = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='IdResposta')  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', unique=True, max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivoResposta'
