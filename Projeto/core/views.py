from django.shortcuts import render

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

def contato(request):
    if request.POST:
        print(request.POST['mensagem'])
    return render(request,"contato.html")
'''
def index(request):
	return render(request, 'index.html')
	
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
	