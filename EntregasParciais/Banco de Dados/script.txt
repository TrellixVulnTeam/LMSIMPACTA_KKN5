/*Vitor Crepaldi Carlessi - 1700266  */
/* Matheus Pereira - 1700688 */
/* Lucas Araújo - 1700424 */
/* Lucas Alves Siqueira - 1700262 */
/* Danilo Lopes do Nascimento - 1700255 */
/* Bruno Lima Dos santos - 1700713  */


/*use master
drop database LMSIMPACTAteste
GO*/
 
create database LMSIMPACTAteste;
GO

use LMSIMPACTAteste;
GO


/*INICIO DA CRIAÇÃO DAS TABELAS*/







CREATE TABLE Disciplina(
	
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


CREATE TABLE Professor(
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


CREATE TABLE GradeCurricular(
	Id SMALLINT  IDENTITY,
	IdCurso int,
	Ano SMALLINT,
	Semestre CHAR(1),
	CONSTRAINT PkIdGradeCurricular PRIMARY KEY (Id),
	CONSTRAINT FkIdGradeCurso FOREIGN KEY (IdCurso) REFERENCES core_curso (Id),
	CONSTRAINT UqGradeCurricular UNIQUE (Ano, Semestre, IdCurso)
);

CREATE TABLE Periodo(
	Id TINYINT IDENTITY,
	IdGradeCurricular SMALLINT NOT NULL,
	Numero TINYINT NOT NULL, 
	CONSTRAINT PkIdPeriodo PRIMARY KEY (Id),
	CONSTRAINT FkIdGradeCurricular FOREIGN KEY (IdGradeCurricular) REFERENCES GradeCurricular(Id),
	CONSTRAINT UqNumero UNIQUE (Numero, IdGradeCurricular)
);


CREATE TABLE DisciplinaOfertada(
	Id SMALLINT IDENTITY,
	IdDisciplina int NOT NULL,
	Ano SMALLINT NOT NULL,
	Semestre CHAR(1) NOT NULL,
	CONSTRAINT PkIdDisciplinaOfertada PRIMARY KEY (Id),
	CONSTRAINT FkIdDisciplina FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(Id),
	CONSTRAINT UqDisciplinaOfertada UNIQUE (IdDisciplina, Ano, Semestre)
);


CREATE TABLE Turma(
	Id INT IDENTITY,
	identificador CHAR(1) NOT NULL, 
	Turno VARCHAR(15),
	Id_DisciplinaOfertada SMALLINT,
	IdProfessor SMALLINT,
	CONSTRAINT PkIdTurma PRIMARY KEY (Id),
	CONSTRAINT FkId_DisciplinaOfertada FOREIGN KEY (Id_DisciplinaOfertada) REFERENCES DisciplinaOfertada(Id),
	CONSTRAINT FkIdProfessor FOREIGN KEY (IdProfessor) REFERENCES Professor(Id),
	CONSTRAINT UqTurma UNIQUE (identificador, id_disciplinaofertada)
);


CREATE TABLE Questao(
	Id INT IDENTITY,
	IdTurma INT NOT NULL,
	Numero INT,
	data_limite_entrega DATE,
	Descricao TEXT,
	Data DATE NOT NULL,
	CONSTRAINT IdQuestao PRIMARY KEY (Id),
	CONSTRAINT FKidTUrma FOREIGN KEY (IdTurma) REFERENCES Turma (Id),
	CONSTRAINT UqNumeroQuestao UNIQUE (Numero, IdTurma)
);


CREATE TABLE Resposta(
	Id INT IDENTITY,
	IdQuestao INT NOT NULL,
	IdAluno INT NOT NULL,
	Data_Avaliacao DATE NOT NULL,
	Nota DECIMAL(4,2),
	Avaliacao TEXT,
	Descricao TEXT,
	Data_de_Envio DATE,
	CONSTRAINT PkIdRespoosta PRIMARY KEY (Id),
	CONSTRAINT FkIdNumeroQuestao FOREIGN KEY (IdQuestao) REFERENCES Questao(ID),
	CONSTRAINT FkIdAlunoQuestao FOREIGN KEY (IdAluno) REFERENCES core_aluno(usuario_ptr_id),
	CONSTRAINT UqResposta UNIQUE (Idquestao, IdAluno)
	
);


CREATE TABLE PeriodoDisciplina(
	Id SMALLINT IDENTITY,
	IdPeriodo TINYINT NOT NULL,
	IdDisciplina int NOT NULL,
	CONSTRAINT PkIdPeriodoDisciplina PRIMARY KEY (Id),
	CONSTRAINT FkIdPeriodo FOREIGN KEY (IdPeriodo) REFERENCES Periodo(Id),
	CONSTRAINT FkIdDisciplinaPerio FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(id),
	CONSTRAINT UQPeriodoDisci UNIQUE (IdPeriodo, IdDisciplina)
);

CREATE TABLE Matricula(
	Id INT IDENTITY,
	IdAluno INT NOT NULL,
	IdTurma INT NOT NULL,
	CONSTRAINT PkIdMatricula PRIMARY KEY (Id),
	CONSTRAINT FkIdAluno FOREIGN KEY (IdAluno) REFERENCES core_aluno(usuario_ptr_id),
	CONSTRAINT FkIdTurmaMa FOREIGN KEY (IdTurma) REFERENCES Turma(Id),
	CONSTRAINT UQMatricula UNIQUE (IdAluno, IdTurma)

);


CREATE TABLE ArquivoResposta(
	IdArquivoResposta INT IDENTITY,
	IdResposta INT NOT NULL,
	Arquivo VARCHAR(500),
	CONSTRAINT PkIdArquivoResposta PRIMARY KEY (IdArquivoResposta), 
	CONSTRAINT FkIdResposta FOREIGN KEY (IdResposta) REFERENCES Resposta(Id),
	CONSTRAINT UqArquivoResposta UNIQUE (Arquivo, IdResposta)
);

CREATE TABLE CursoTurma(
	Id SMALLINT IDENTITY,
	IdCurso int NOT NULL,
	IdTurma INT NOT NULL,
	CONSTRAINT PkIdCursoTurma PRIMARY KEY (Id),
	CONSTRAINT FkIdCursoTurma FOREIGN KEY (IdCurso) REFERENCES core_curso(Id),
	CONSTRAINT FkIdTurmaCursoTurma FOREIGN KEY (IdTurma) REFERENCES Turma(Id),
	Constraint UQTurmaCurso UNIQUE (IdCurso, IdTurma)
);


CREATE TABLE ArquivoQuestao(
	Id INT IDENTITY,
	IdQuestao INT NOT NULL,
	Arquivo VARCHAR(500) NOT NULL,
	CONSTRAINT PkIdArquivoQuestao PRIMARY KEY (Id),
	CONSTRAINT FkIdQuestaoArquivoQuestao FOREIGN KEY (IdQuestao) REFERENCES Questao(Id),
	CONSTRAINT UqArquivoQuestao UNIQUE (Arquivo, IdQuestao)
);


