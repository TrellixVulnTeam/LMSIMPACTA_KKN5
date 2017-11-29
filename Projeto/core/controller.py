from django.db import models
from core.models import Resposta
from core.models import Aluno
from core.models import Questao
from core.models import Disciplinaofertada
from core.models import Matricula
from core.models import Resposta
from core.models import Turma
from core.models import Curso
from datetime import date


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
def calculamedia(aluno):
    nota=0
    quant=0
    entregues=Resposta.objects.filter(idaluno=aluno)
    for entregue in entregues:
        nota+= entregue.nota
        quant+=1
    return nota/quant   

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
    dataatual= date.today()
    ValidaQuestao = Questao.objects.filter(id=Id)
    for q in ValidaQuestao:
        if q.data_limite_entrega < dataatual:
            return "Passou da data de entrega"
        else:
            return "Pode fazer"

def ValidaMatricula(IdAluno,iddisc):
    matriculadoem=[]
    verify=[]
    Matriculas = Matricula.objects.filter(idaluno=IdAluno)
    for matricula in Matriculas:
        matriculadoem.append(matricula.values)

    TurmaMatriculado = Turma.objects.filter(id__in=matriculadoem)

    for turma in TurmaMatriculado:
        if turma.id_disciplinaofertada == iddisc:
            mtriculadoem.append(iddisc)
    if len(matriculadoem)>=1:
        return "você já não pode se matricular"
    else:
        return "pode se matricular"




    if teste.count:
        return "Já possui matricula nesse disciplina"
    else:
        return "pode metricular"






def CrudMatricula():
    u = Aluno(ra = "12312",nome = "dsydg",email = "uhsdah",celular = "12323",idcurso = 1)
    u.save()
    return ("funfo")



    