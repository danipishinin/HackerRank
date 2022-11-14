-- with é uma palavra reservada do SQL para criar uma CTE (Common Table Expression)

-- Uma CTE é muito parecida com uma tabela derivada que não é armazenada como um objeto e que existe apenas durante a execução da consulta.

-- A clausula OVER determina o particionamento e a ordenação de um conjunto de linhas antes da aplicação da função de janela associada

-- Partition By: particiona os resultados da consulta, no caso abaixo, por ocupação.

-- The ROW_NUMBER() function uses the OVER and PARTITION BY clause and sorts results in ascending or descending order. 

WITH cte AS ( SELECT *, ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS occupation_row 
            FROM occupations)

SELECT MAX(CASE WHEN Occupation = 'Doctor' THEN Name END) AS Doctors
     , MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professors
     , MAX(CASE WHEN Occupation = 'Singer' THEN Name END)    AS Singers
     , MAX(CASE WHEN Occupation = 'Actor' THEN Name END)     AS Actors

FROM cte 
GROUP BY occupation_row