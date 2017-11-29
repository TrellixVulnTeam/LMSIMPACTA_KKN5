from django.db import models
from core.models import Resposta
from core.models import Aluno
from core.models import Questao
from core.models import Disciplinaofertada
from core.models import Matricula
from core.models import Resposta
from core.models import Turma
from core.models import Curso
from datetime import datetime


# Create your models here.
'''
class Curso(models.Model):

    nome = models.CharField("Nome",max_length=50)
    carga_horaria = models.IntegerField("Carga Horária")
    professor = models.CharField("Coordenador",max_length=50)
    tipo = models.CharField("Tipo",max_length=50)

    descricao = models.TextField("Descrição",blank=True)
    ativo = models.BooleanField("Ativo?",default=True)

    def __str__(self):
        return self.nome
'''
def AplicaTeste(user):
    
    if Resposta.objects.filter(idaluno=user.ra):
        return " ja fez o teste"
    else:
        return "renderizar o teste"

    
def Aluno_Enviaram():

    ListaDosQueFizeram = []
    listaNome=[]
    AlunosResponderam = Resposta.objects.all()
    TodosAlunos = Aluno.objects.all()
    for aluno in TodosAlunos:
        for AlunoRespondeu in AlunosResponderam:
            if aluno.id == AlunoRespondeu.raaluno:
                ListaDosQueFizeram.append(aluno.nome)
    return ListaDosQueFizeram

def Alunos_N_Enviaram():
    ListaDosQueFizeram = []
    listaNome=[]
    AlunosResponderam = Resposta.objects.all()
    for AlunoRespondeu in AlunosResponderam:
        ListaDosQueFizeram.append(AlunoRespondeu.raaluno)
    TodosAlunos = Aluno.objects.exclude(id__in=ListaDosQueFizeram)
    return TodosAlunos

def VerificaPrazo(Id):
    dataatual= datetime.now()
    ValidaQuestao = Questao.objects.filter(id=2)
    if ValidaQuestao.data > dataatual:
        return print ( "você não pode entregar a questão pois passou da data limite")
    else:
        return "Grud resposta"

def ValidaMatricula(Aluno,IdDisciplina):
    Matriculas = Matricula.objects.all()
    Disciplinas = Disciplinaofertada.objects.all()
    turmas = turma.objects.all()
    for matricula in Matriculas:
        for turma in turmas:
            if matricula.idTurma == turma.idTurma:
                if turma.id_disciplinaofertada == IdDisciplina:
                    print("Já possui matricula nesse disciplina")
                    break
                else:
                    print ("pode metricular")

def CrudMatricula():
    u = Aluno(ra = "12312",nome = "dsydg",email = "uhsdah",celular = "12323",idcurso = 1)
    u.save()
    return ("funfo")