from django.db import models
from core.modelos import Resposta
from core.modelos import Aluno
from core.modelos import Questao
from core.modelos import Disciplinaofertada
from core.modelos import Matricula
from core.modelos import Resposta
from core.modelos import Turma

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
def AplicaTeste(self,Aluno):
   AlunosResponderam = Resposta.objects.all()
   for Ra in AlunosQueFizeram.Ra:
       if RA == Aluno.RA:
           return print ("Já fez o teste") 
    else:
        return "teste"
    

def Aluno_Enviaram(self,Aluno):
    AlunosResponderam = Resposta.objects.all()
    TodosAlunos = Aluno.objects.all()
    for aluno in TodosAlunos:
        for AlunoRespondeu in AlunosResponderam:
            if aluno.Ra == AlunoRespondeu.Ra:
                ListaDosQueFizeram.append(TodosAlunos.Nome)
    return ListaDosQueFizeram

def Alunos_N_Enviaram(self,Aluno):
    AlunosQueResponderam = Resposta.objects.all()
    TodosAlunos = Aluno.objects.all()
    for Aluno in TodosAlunos:
        for AlunoRespondeu in AlunosResponderam:
            if Aluno.Ra != AlunoRespondeu.Ra:
                ListaDosQueNaoFizeram.append(TodosAlunos.nome)
    return ListaDosQueNaoFizeram

def VerificaPrazo(self,dataatual,Questao):
    ValidaQuestao = Questao.objects.all()
    if ValidaQuestao.data_limite_entrega > dataatual:
        return print ( "você não pode entregar a questão pois passou da data limite")
    else:
        return "Grud resposta"

def ValidaMatricula(self,Aluno,IdDisciplina):
    Matriculas = Matricula.objects.all()
    Disciplinas = Disciplinaofertada.objects.all()
    turmas = turma.objects.all()
    for matricula in Matriculas:
       for turma in turmas:
           if matricula.idTurma == turma.idTurma:
               if  turma.id_disciplinaofertada == IdDisciplina:
                   print("Já possui matricula nesse disciplina")
                   break
                else:
                    print ("pode metricular")






