--3.3. Estruturar tabelas necessárias para o arquivo csv.
CREATE TABLE DemonstracoesContabeis (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    DATA DATE,
    REG_ANS VARCHAR(20),
    CD_CONTA_CONTABIL VARCHAR(20),
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(18, 2),
    VL_SALDO_FINAL DECIMAL(18, 2)
);

--3.4. Importar o conteúdo dos arquivos preparados.
LOAD DATA INFILE './operadoras_ativas_ans.csv'
INTO TABLE DemonstracoesContabeis
CHARACTER SET utf8mb4  
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  
LINES TERMINATED BY '\n' 
IGNORE 1 LINES  
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);  

-- 3.5. 10 operadoras com maiores despesas 
SELECT Operadora, SUM(Despesas) AS Total_Despesas
FROM DemonstracoesContabeis
GROUP BY Operadora
ORDER BY Total_Despesas DESC
LIMIT 10;

-- 3.5. 10 operadoras com maiores despesas nessa categoria no último ano
SELECT Operadora, SUM(Despesas) AS Total_Despesas
FROM DemonstracoesContabeis
WHERE Categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND DATA BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR) AND CURRENT_DATE()
GROUP BY Operadora
ORDER BY Total_Despesas DESC
LIMIT 10;

-- Salvar resultados da consulta em um arquivo CSV
SELECT Operadora, SUM(Despesas) AS Total_Despesas
INTO OUTFILE './BancoDados/csv_files/relatorio.csv' 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
FROM DemonstracoesContabeis
GROUP BY Operadora
ORDER BY Total_Despesas DESC
LIMIT 10;



