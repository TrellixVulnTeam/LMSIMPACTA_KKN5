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

from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    
    def _criar_usuario(self, ra, password, **campos):
        if not ra: 
            raise ValueError("RA deve ser declarado!")
        user = self.model(ra=ra, **campos)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **campos):
        return self._criar_usuario(ra, password, **campos)

    def create_superuser(self, ra, password=None, **campos):
        campos.setdefault('perfil', 'C')
        return self._criar_usuario(ra, password, **campos)


# Create your models here.
class Curso(models.Model):

    id = models.IntegerField("Id",unique=True,primary_key=True)
    sigla= models.CharField("Sigla",max_length=5)
    nome=models.CharField("Nome",max_length=50)

    def __str__(self):
        return self.nome

class Usuario(AbstractBaseUser):

    ra = models.IntegerField("RA",unique=True)
    password = models.CharField("Senha", max_length=200)

    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-Mail", max_length=50)

    perfil = models.CharField("Perfil", max_length=1)
    ativo = models.BooleanField("Ativo", default=True)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome','email']

    objects = UsuarioManager()

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def __str__(self):
        return self.nome

    @property
    def is_staff(self):
        return self.perfil == "C"

    def has_module_perms(self, package_name):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

class Aluno(Usuario):

    celular = models.CharField("Celular", max_length=11)
    curso = models.ForeignKey(Curso)



class Arquivoquestao(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idquestao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='IdQuestao')  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivoQuestao'
        unique_together = (('arquivo', 'idquestao'),)


class Arquivoresposta(models.Model):
    idarquivoresposta = models.AutoField(db_column='IdArquivoResposta', primary_key=True)  # Field name made lowercase.
    idresposta = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='IdResposta')  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivoResposta'
        unique_together = (('arquivo', 'idresposta'),)


class Cursoturma(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey('CoreCurso', models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CursoTurma'
        unique_together = (('idcurso', 'idturma'),)


class Disciplina(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True, max_length=240)  # Field name made lowercase.
    teoria = models.DecimalField(db_column='Teoria', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pratica = models.DecimalField(db_column='Pratica', max_digits=3, decimal_places=0)  # Field name made lowercase.
    cargahoraria = models.SmallIntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    ementa = models.TextField(db_column='Ementa')  # Field name made lowercase. This field type is a guess.
    competencias = models.TextField(db_column='Competencias')  # Field name made lowercase. This field type is a guess.
    habilidades = models.TextField(db_column='Habilidades')  # Field name made lowercase. This field type is a guess.
    conteudo = models.TextField(db_column='Conteudo')  # Field name made lowercase. This field type is a guess.
    bibliografia_basica = models.TextField(db_column='Bibliografia_basica', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bibliografia_complementar = models.TextField(db_column='Bibliografia_complementar', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Disciplina'


class Disciplinaofertada(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    ano = models.SmallIntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.CharField(db_column='Semestre', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisciplinaOfertada'
        unique_together = (('iddisciplina', 'ano', 'semestre'),)


class Gradecurricular(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey('CoreCurso', models.DO_NOTHING, db_column='IdCurso', blank=True, null=True)  # Field name made lowercase.
    ano = models.SmallIntegerField(db_column='Ano', blank=True, null=True)  # Field name made lowercase.
    semestre = models.CharField(db_column='Semestre', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GradeCurricular'
        unique_together = (('ano', 'semestre', 'idcurso'),)


class Matricula(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey('CoreAluno', models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Matricula'
        unique_together = (('idaluno', 'idturma'),)


class Periodo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idgradecurricular = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='IdGradeCurricular')  # Field name made lowercase.
    numero = models.SmallIntegerField(db_column='Numero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Periodo'
        unique_together = (('numero', 'idgradecurricular'),)


class Periododisciplina(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idperiodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='IdPeriodo')  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodoDisciplina'
        unique_together = (('idperiodo', 'iddisciplina'),)


class Professor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA', unique=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=120)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11, blank=True, null=True)  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Professor'


class Questao(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    data_limite_entrega = models.CharField(max_length=10, blank=True, null=True)
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data = models.CharField(db_column='Data', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questao'
        unique_together = (('numero', 'idturma'),)


class Resposta(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idquestao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='IdQuestao')  # Field name made lowercase.
    idaluno = models.ForeignKey('CoreAluno', models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    data_avaliacao = models.CharField(db_column='Data_Avaliacao', max_length=10)  # Field name made lowercase.
    nota = models.DecimalField(db_column='Nota', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    avaliacao = models.TextField(db_column='Avaliacao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data_de_envio = models.CharField(db_column='Data_de_Envio', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Resposta'
        unique_together = (('idquestao', 'idaluno'),)


class Turma(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    identificador = models.CharField(max_length=1)
    turno = models.CharField(db_column='Turno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    id_disciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Id_DisciplinaOfertada', blank=True, null=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='IdProfessor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Turma'
        unique_together = (('identificador', 'id_disciplinaofertada'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CoreAluno(models.Model):
    usuario_ptr = models.ForeignKey('CoreUsuario', models.DO_NOTHING, primary_key=True,unique=True)
    celular = models.CharField(max_length=11)
    curso = models.ForeignKey('CoreCurso', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_aluno'


class CoreCurso(models.Model):
    id = models.IntegerField(primary_key=True)
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'core_curso'


class CoreUsuario(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    ra = models.IntegerField(unique=True)
    password = models.Field(max_length=200)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    perfil = models.CharField(max_length=1)
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'core_usuario'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(CoreUsuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
