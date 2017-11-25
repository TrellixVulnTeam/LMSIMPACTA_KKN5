/*Vitor Crepaldi Carlessi - 1700266  */
/* Matheus Pereira - 1700688 */
/* Lucas Araújo - 1700424 */
/* Lucas Alves Siqueira - 1700262 */
/* Danilo Lopes do Nascimento - 1700255 */
/* Bruno Lima Dos santos - 1700713  */


/*use master
drop database LMSIMPACTA
GO*/
 
create database LMSIMPACTA;
GO

use LMSIMPACTA;
GO

CREATE SCHEMA Faculdade;
GO


/*INICIO DA CRIAÇÃO DAS TABELAS*/


CREATE TABLE Faculdade.curso (

	Id smallint identity,
	Sigla VARCHAR(5) NOT NULL,
	Nome VARCHAR(50) NOT NULL,
	CONSTRAINT PkIdCurso PRIMARY KEY (Id),
	CONSTRAINT UQSiglaCurso UNIQUE (Sigla),
	CONSTRAINT UQNomeCurso UNIQUE (Nome)
);


CREATE TABLE Faculdade.Aluno(

	Id INT identity,
	IdCurso smallint,
	RA INT NOT NULL,
	Nome VARCHAR(120) NOT NULL,
	Email VARCHAR(80) NOT NULL,
	Celular CHAR(11),
	CONSTRAINT PkIdAluno PRIMARY KEY (Id),
	CONSTRAINT FKIdCurso FOREIGN KEY (IdCurso) REFERENCES Faculdade.CURSO (Id),
	CONSTRAINT UQRaAluno UNIQUE (RA)

);


CREATE TABLE Faculdade.Disciplina(
	
	Id int IDENTITY,
	Nome VARCHAR(240) NOT NULL,
	Teoria DECIMAL (3) NOT NULL,
	Pratica DECIMAL (3) NOT NULL,
	CargaHoraria TINYINT NOT NULL,
	Ementa TEXT NOT NULL,
	Competencias TEXT NOT NULL,
	Habilidades TEXT NOT NULL,
	Conteudo TEXT NOT NULL,
	Bibliografia_basica TEXT,
	Bibliografia_complementar TEXT,
	CONSTRAINT PkIdDisciplina PRIMARY KEY (Id),
	CONSTRAINT UqNomeDisciplina UNIQUE (Nome)
);


CREATE TABLE Faculdade.Professor(
	Id SMALLINT IDENTITY,
	RA INT NOT NULL,
	Nome VARCHAR(120) NOT NULL,
	Email VARCHAR(80) NOT NULL,
	Celular CHAR(11),
	Apelido VARCHAR(30)
	CONSTRAINT PkIdProfessor PRIMARY KEY (ID),
	CONSTRAINT UqRaProfessor UNIQUE (RA),
	CONSTRAINT UqApelidoProfessor  UNIQUE (Apelido)
);


CREATE TABLE Faculdade.GradeCurricular(
	Id SMALLINT  IDENTITY,
	IdCurso smallint,
	Ano SMALLINT,
	Semestre CHAR(1),
	CONSTRAINT PkIdGradeCurricular PRIMARY KEY (Id),
	CONSTRAINT FkIdGradeCurso FOREIGN KEY (IdCurso) REFERENCES Faculdade.Curso (Id),
	CONSTRAINT UqGradeCurricular UNIQUE (Ano, Semestre, IdCurso)
);

CREATE TABLE Faculdade.Periodo(
	Id TINYINT IDENTITY,
	IdGradeCurricular SMALLINT NOT NULL,
	Numero TINYINT NOT NULL, 
	CONSTRAINT PkIdPeriodo PRIMARY KEY (Id),
	CONSTRAINT FkIdGradeCurricular FOREIGN KEY (IdGradeCurricular) REFERENCES Faculdade.GradeCurricular(Id),
	CONSTRAINT UqNumero UNIQUE (Numero, IdGradeCurricular)
);


CREATE TABLE Faculdade.DisciplinaOfertada(
	Id SMALLINT IDENTITY,
	IdDisciplina int NOT NULL,
	Ano SMALLINT NOT NULL,
	Semestre CHAR(1) NOT NULL,
	CONSTRAINT PkIdDisciplinaOfertada PRIMARY KEY (Id),
	CONSTRAINT FkIdDisciplina FOREIGN KEY (IdDisciplina) REFERENCES Faculdade.Disciplina(Id),
	CONSTRAINT UqDisciplinaOfertada UNIQUE (IdDisciplina, Ano, Semestre)
);


CREATE TABLE Faculdade.Turma(
	Id INT IDENTITY,
	identificador CHAR(1) NOT NULL, 
	Turno VARCHAR(15),
	Id_DisciplinaOfertada SMALLINT,
	IdProfessor SMALLINT,
	CONSTRAINT PkIdTurma PRIMARY KEY (Id),
	CONSTRAINT FkId_DisciplinaOfertada FOREIGN KEY (Id_DisciplinaOfertada) REFERENCES Faculdade.DisciplinaOfertada(Id),
	CONSTRAINT FkIdProfessor FOREIGN KEY (IdProfessor) REFERENCES Faculdade.Professor(Id),
	CONSTRAINT UqTurma UNIQUE (identificador, id_disciplinaofertada)
);


CREATE TABLE Faculdade.Questao(
	Id INT IDENTITY,
	IdTurma INT NOT NULL,
	Numero INT,
	data_limite_entrega DATE,
	Descricao TEXT,
	Data DATE NOT NULL,
	CONSTRAINT IdQuestao PRIMARY KEY (Id),
	CONSTRAINT FKidTUrma FOREIGN KEY (IdTurma) REFERENCES Faculdade.Turma (Id),
	CONSTRAINT UqNumeroQuestao UNIQUE (Numero, IdTurma)
);


CREATE TABLE Faculdade.Resposta(
	Id INT IDENTITY,
	IdQuestao INT NOT NULL,
	IdAluno INT NOT NULL,
	Data_Avaliacao DATE NOT NULL,
	Nota DECIMAL(4,2),
	Avaliacao TEXT,
	Descricao TEXT,
	Data_de_Envio DATE,
	CONSTRAINT PkIdRespoosta PRIMARY KEY (Id),
	CONSTRAINT FkIdNumeroQuestao FOREIGN KEY (IdQuestao) REFERENCES Faculdade.Questao(ID),
	CONSTRAINT FkIdAlunoQuestao FOREIGN KEY (IdAluno) REFERENCES Faculdade.Questao(ID),
	CONSTRAINT UqResposta UNIQUE (Idquestao, IdAluno)
	
);


CREATE TABLE Faculdade.PeriodoDisciplina(
	Id SMALLINT IDENTITY,
	IdPeriodo TINYINT NOT NULL,
	IdDisciplina int NOT NULL,
	CONSTRAINT PkIdPeriodoDisciplina PRIMARY KEY (Id),
	CONSTRAINT FkIdPeriodo FOREIGN KEY (IdPeriodo) REFERENCES Faculdade.Periodo(Id),
	CONSTRAINT FkIdDisciplinaPerio FOREIGN KEY (IdDisciplina) REFERENCES Faculdade.Disciplina(id),
	CONSTRAINT UQPeriodoDisci UNIQUE (IdPeriodo, IdDisciplina)
);

CREATE TABLE Faculdade.Matricula(
	Id INT IDENTITY,
	IdAluno INT NOT NULL,
	IdTurma INT NOT NULL,
	CONSTRAINT PkIdMatricula PRIMARY KEY (Id),
	CONSTRAINT FkIdAluno FOREIGN KEY (IdAluno) REFERENCES Faculdade.Aluno(Id),
	CONSTRAINT FkIdTurmaMa FOREIGN KEY (IdTurma) REFERENCES Faculdade.Turma(Id),
	CONSTRAINT UQMatricula UNIQUE (IdAluno, IdTurma)

);


CREATE TABLE Faculdade.ArquivoResposta(
	IdArquivoResposta INT IDENTITY,
	IdResposta INT NOT NULL,
	Arquivo VARCHAR(500),
	CONSTRAINT PkIdArquivoResposta PRIMARY KEY (IdArquivoResposta), 
	CONSTRAINT FkIdResposta FOREIGN KEY (IdResposta) REFERENCES Faculdade.Resposta(Id),
	CONSTRAINT UqArquivoResposta UNIQUE (Arquivo, IdResposta)
);

CREATE TABLE Faculdade.CursoTurma(
	Id SMALLINT IDENTITY,
	IdCurso smallint NOT NULL,
	IdTurma INT NOT NULL,
	CONSTRAINT PkIdCursoTurma PRIMARY KEY (Id),
	CONSTRAINT FkIdCursoTurma FOREIGN KEY (IdCurso) REFERENCES Faculdade.Curso(Id),
	CONSTRAINT FkIdTurmaCursoTurma FOREIGN KEY (IdTurma) REFERENCES Faculdade.Turma(Id),
	Constraint UQTurmaCurso UNIQUE (IdCurso, IdTurma)
);


CREATE TABLE Faculdade.ArquivoQuestao(
	Id INT IDENTITY,
	IdQuestao INT NOT NULL,
	Arquivo VARCHAR(500) NOT NULL,
	CONSTRAINT PkIdArquivoQuestao PRIMARY KEY (Id),
	CONSTRAINT FkIdQuestaoArquivoQuestao FOREIGN KEY (IdQuestao) REFERENCES Faculdade.Questao(Id),
	CONSTRAINT UqArquivoQuestao UNIQUE (Arquivo, IdQuestao)
);
 

