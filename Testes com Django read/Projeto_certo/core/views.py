from django.shortcuts import render

# Create your views here.
def index(aplicacao):
    artigos = { "cursos" : [
        "teste",
        "banana",
        "maconha",
    ]



        # "populares" : [
        #    "Como bater ponto pelo computador?",
        #    "Como cadastrar novas Escalas?",
        #   "Como cadastrar novos locais de trabalho?",
        #    "Como cadastrar novos Funcionários?",
        #    "Como cadastrar novos Funcionários?",
        # ]
        
    }
    return render(aplicacao, "index.html", artigos)