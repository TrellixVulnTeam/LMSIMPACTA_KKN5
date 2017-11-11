from django.contrib import admin


from core.modelos import Aluno, Disciplina, Curso

# Register your models here.
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Aluno)
