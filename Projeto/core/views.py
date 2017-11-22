from django.shortcuts import render
from django.core.mail import send_mail
from core.models import *



def index(request):
    novo = Alunos_N_Enviaram()
    contexto = {
        "cursos": Aluno.objects.all(),
        "faculdade":novo,
        "pagina":"Homepage",
        "usuario":"Yuri",
        "logado":True,
        "idade":-18
        }
    return render(request, 'index.html',contexto)
	
def login(request):
	return render(request, 'login.html')
	
def esquecisenha(request):
	return render(request, 'esquecisenha.html')
	
def contato(request):
	return render(request, 'contato.html')
	
def cadastro(request):
	return render(request, 'cadastro.html')
	
def aluno(request):
	return render(request, "aluno.html")


