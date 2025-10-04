-- Arquivo: consultas_sql.sql
-- Explicação da Lógica: As consultas assumem que o dataset importado 
-- (data_clean.csv) está na tabela VENDAS.

-- 1. Listar o nome do produto, categoria e a soma total de vendas
--    (Quantidade * Preço) para cada produto, ordenado pelo valor total em DESC.
-- Lógica: Agrupar os resultados por Produto e Categoria e usar a função SUM() 
-- para agregar o Total de Vendas (Quantidade * Preco). A ordenação é feita 
-- de forma decrescente para destacar os líderes de venda.
SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS Soma_Total_Vendas
FROM
    VENDAS
GROUP BY
    Produto, Categoria
ORDER BY
    Soma_Total_Vendas DESC;


-- 2. Identificar os produtos que venderam menos no mês de junho de 2024.
-- Lógica: Utilizei a função EXTRACT() do PostgreSQL para filtrar os registros 
-- especificamente para o mês 6 (Junho). Como os dados são de 2023, usei 
-- o ano de 2023 na cláusula WHERE. Agrupei por Produto e ordenei de forma 
-- crescente (ASC) para destacar os que venderam menos, limitando aos 5 piores.


SELECT
    Produto,
    SUM(Quantidade * Preco) AS Soma_Total_Vendas_Junho
FROM
    VENDAS
WHERE
    EXTRACT(YEAR FROM Data) = 2023 AND EXTRACT(MONTH FROM Data) = 6 
GROUP BY
    Produto
ORDER BY
    Soma_Total_Vendas_Junho ASC 
LIMIT 5;