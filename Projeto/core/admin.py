from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from core.models import *

class CursoAdmin(admin.ModelAdmin):
    list_display=["nome","sigla"]

class AlunoForm(forms.ModelForm):

    def save(self, commit=True):
        aluno = super(AlunoForm,self).save(commit=False)
        aluno.set_password("123@mudar")
        aluno.perfil = 'A'
        if commit:
            aluno.save()
        return aluno

    class Meta:
        model = Aluno
        fields = ["ra", "nome", "email", "curso"]

class AlunoAlterarForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ["nome", "email", "curso"]
        
class AlunoAdmin(UserAdmin):
    add_form = AlunoForm
    form = AlunoAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "nome", "email", "curso")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "curso")}),)
    list_display = ["ra","nome","email","curso"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["curso"]



# Register your models here.
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Arquivoquestao)
admin.site.register(Arquivoresposta)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Cursoturma)
admin.site.register(Disciplina)
admin.site.register(Disciplinaofertada)
admin.site.register(Gradecurricular)
admin.site.register(Periodo)
admin.site.register(Periododisciplina)
admin.site.register(Professor)
admin.site.register(Questao)
admin.site.register(Resposta)
admin.site.register(Turma)