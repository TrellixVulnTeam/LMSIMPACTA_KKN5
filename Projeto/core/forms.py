from django import forms
from core.models import Questao, Curso, CoreAluno  

class QuestaoForm(forms.ModelForm):
    
    class Meta:
        model = Questao
        fields = "__all__"


class Matricula(forms.ModelForm):

    class Meta:
        model = CoreAluno
        fields = "__all__"
