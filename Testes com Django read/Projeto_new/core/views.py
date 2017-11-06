from django.shortcuts import render

# Create your views here.
def index(requisicao):
    return render(requisicao,'index.html')