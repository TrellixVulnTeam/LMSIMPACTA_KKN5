from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from core.models import Aluno
from core.forms import Matricula, QuestaoForm
from core.controller import *

from core.modelos import *
'''from core.models import Curso

def banana(requisicao):
    contexto = {
        "cursos": Curso.objects.all(),
        "faculdade":"Faculdade Impacta de Tecnologia",
        "pagina":"Homepage",
        "usuario":"Yuri",
        "logado":True,
        "idade":-18
    }
    return render(requisicao,"index.html",contexto)

...def contato(request):
    if request.POST:
        print(request.POST['mensagem'])
    return render(request,"contato.html")
'''
def index(request):

    novo =  calculamedia(request.user.id)
    
    contexto = {
        "cursos":novo,
        "faculdade":'novo',
        "pagina":"Homepage",
        "usuario":"Yuri",
        "logado":True,
        "idade":-18
        }
    return render(request, 'index.html',contexto)
	
def checa_aluno(usuario):
    return usuario.perfil == "A"

def checa_professor(usuario):
    return usuario.perfil == "P"    
	
def esquecisenha(request):
	return render(request, 'esquecisenha.html')




def contato(request):   
	return render(request, 'contato.html')


def login(request):   
	return render(request, 'login.html')    



@login_required(login_url="/login")
@user_passes_test(checa_professor)
def professor(request):   
	return render(request, 'professor.html')
	


def cadastro(request):
	return render(request, 'cadastro.html')


def restrito(request):
    return render (request,'restrito.html')

@login_required(login_url="/login")
@user_passes_test(checa_professor)
def questao_form(request) :
    form = QuestaoForm(request.POST,request.FILES)
    if request.POST:
        #form = QuestaoForm()
            if form.is_valid():
                form.save()
                return redirect("/professor")
    contexto={
        "form":form
        }
    return render(request,'questao_form.html',contexto)    

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def aluno(request):
    teste = Aluno.objects.get(id=request.user.id)
    contexto = {
        "alunos":teste.ra ,
        "faculdade":'novo',
        "pagina":"Homepage",
        "usuario":"Yuri",
        "logado":True,
        "idade":-18
        }
    
    return render(request, "Aluno.html",contexto)


def matricula(request):
    form = Matricula(request.POST, request.FILES)
    if request.POST:
        if form.is_valid():
            form.save() 
            return redirect("/matricula")
    contexto = {
        "form":form
            }
    return render(request, "matricula.html", contexto)



"""send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)"""