from django.db import models

# Create your models here.
class Curso(models.Model):

    nome = models.CharField("Nome",max_length=50)
    carga_horaria = models.IntegerField("Carga Horária")
    professor = models.CharField("Coordenador",max_length=50)
    tipo = models.CharField("Tipo",max_length=50)

    descricao = models.TextField("Descrição",blank=True)
    ativo = models.BooleanField("Ativo?",default=True)

    def __str__(self):
        return self.nome
