/* Use master */

Use LMSIMPACTA

/*Exercicio 1*/

SELECT 
	A.Nome AS Nome,
	A.Email AS Email,
	A.RA AS RA
FROM
	Faculdade.Aluno AS A
	JOIN
	Faculdade.Curso AS C
	ON(A.IdCurso = C.Id)
WHERE
	C.Sigla = 'SI'


/*Exercicio 2*/

SELECT 
	C.Sigla,
	D.Nome,
	GC.Ano,
	GC.Semestre
	
FROM
	Faculdade.Disciplina AS D
	JOIN
	Faculdade.GradeCurricular AS GC
	ON(D.Id = GC.Id)
	JOIN
	Faculdade.Curso AS C
	ON(C.Id = GC.IdCurso)
WHERE
	C.Sigla = 'SI' AND GC.Semestre = '1'


/*Exercicio 4*/
SELECT 
	D.Nome,
	Count(A.RA) AS 'Total de Turmas'
FROM
	Faculdade.Aluno AS A
	JOIN
	Faculdade.Matricula AS M
	ON (A.Id =  M.IdAluno)
	JOIN
	Faculdade.Turma AS T
	ON(T.Id = M.IdTurma)
	JOIN
	Faculdade.DisciplinaOfertada AS DO
	ON(DO.Id = T.Id_DisciplinaOfertada)
	JOIN
	Faculdade.Disciplina AS D
	ON(DO.IdDisciplina = D.Id)

WHERE
	DO.Ano = '2017' AND DO.Semestre = '2'

GROUP BY
	D.Nome 
ORDER BY
	D.Nome DESC
	

/*Exercicio 5*/
SELECT
	COUNT(A.RA) AS 'Total de Alunos Matriculados'

FROM
	Faculdade.Matricula AS M
	LEFT JOIN 
	Faculdade.Aluno AS A
	ON(M.IdAluno = A.Id)
	LEFT JOIN 
	Faculdade.Turma AS T
	ON(M.IdTurma = T.Id)
	LEFT JOIN
	Faculdade.DisciplinaOfertada AS DO
	ON(T.Id_DisciplinaOfertada = DO.Id)

WHERE 
	Ano = CONVERT(VARCHAR(4), GetDate(), 120) 

/*Exercicio 6 */
SELECT 
	Q.Numero AS 'Numero da Questão',
	Q.Descricao AS 'Descrição',
	A.Nome AS 'Nome do Aluno',
	A.RA AS 'RA',
	R.Data_de_Envio AS 'Data de Envio'
FROM
	Faculdade.Questao AS Q
	JOIN
	Faculdade.Resposta AS R
	ON (R.IdQuestao = Q.Id)
	JOIN 
	Faculdade.Aluno AS A
	ON (A.Id = R.IdAluno)
		
/*Exercicio 7*/
DECLARE @X INT
SET @X = (SELECT 
				COUNT(P.Id)
			FROM
				Faculdade.Professor AS P);
SELECT 
	@X AS 'Total de Professores Cadastrados',
	COUNT(P.Id) AS 'Total de Professores que dão aula neste Semestre'

FROM
	Faculdade.Professor AS P
WHERE
	P.Id IN (
			SELECT
				P.Id
			FROM
				Faculdade.Professor AS P
				JOIN
				Faculdade.Turma AS T
				ON(P.Id = T.IdProfessor)
				JOIN
				Faculdade.DisciplinaOfertada AS DO
				ON(DO.Id = T.Id_DisciplinaOfertada)
				JOIN
				Faculdade.Disciplina AS D
				ON(DO.IdDisciplina = D.Id)
			WHERE
				Ano = CONVERT(VARCHAR(4), GETDATE(), 120)
		);



/*Exercicio 8*/
SELECT 
	C.Nome,
	COUNT(A.Id) AS Alunos
FROM
	Faculdade.Aluno AS A
	LEFT JOIN
	Faculdade.Curso AS C
	ON(A.IdCurso = C.Id)
GROUP BY
	C.Nome
ORDER BY
	Alunos DESC


/*Exercicio 9
DECLARE @Soma INT
SET @Soma = (
	SELECT 
	SUM(R1.Nota)
	FROM
	Resposta AS R1
	WHERE
	Nota = '7' OR Nota > '7'
);

DECLARE @Total INT
SET @Total=(
	SELECT	
	R2.Nota
	FROM
	Resposta AS R2
);

SELECT
	((@Soma * 100) /@Total) AS 'Percentual de aprovados'
*/

/*
SELECT 
	C.Sigla AS 'Nome do Curso',
	GC.Id AS 'Grade Curricular',
	P.Id AS 'Periodo Semestre',
	PD.IdDisciplina AS 'Total de Disciplinas'
FROM 
	GradeCurricular AS GC
	JOIN 
	Curso AS C
	ON(C.Id = GC.IdCurso)
	JOIN
	Periodo AS P
	ON(P.IdGradeCurricular = GC.Id)
	JOIN
	PeriodoDisciplina AS PD
	ON (P.Id = PD.IdPeriodo)

WHERE
	PD.IdDisciplina IN (
	
	
		SELECT 
			C.Sigla
			
		FROM
				GradeCurricular AS GC
				JOIN 
				Curso AS C
				ON(C.Id = GC.IdCurso)
				JOIN
				Periodo AS P
				ON(P.IdGradeCurricular = GC.Id)
				JOIN
				PeriodoDisciplina AS PD
				ON (P.Id = PD.IdPeriodo)

		GROUP BY
			C.Sigla
	
	);
*/







