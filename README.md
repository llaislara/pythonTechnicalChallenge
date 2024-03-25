# Desafio Técnico

Este é um projeto criado para atender aos requisitos de um processo seletivo. O projeto está dividido em quatro etapas e foi escrito em Python. 




## Etapa 1: Web Scraping e Etapa 2: Extração de Dados de PDF

Esta etapa exemplifica o processo de web scraping em arquivos PDF para extrair dados tabulares e salvá-los em um arquivo CSV. Além disso, automatiza a compactação desse arquivo CSV em um arquivo ZIP. O projeto fornece um script em Python para realizar essas operações de forma eficiente.

### Requisitos

- Python 3.x
- Bibliotecas Python e Módulos: pdfplumber, pandas

Você pode instalar as dependências executando:

```bash
pip install pdfplumber pandas
```

### Uso
1. Coloque seus arquivos PDF na pasta pdf_files.
2. Execute o script `extract_data.py`.
3. Os dados PDF extraídos serão salvos em um arquivo PDF na pasta `pdf_files`.
4. Os dados csv extraídos serão salvos em um arquivo CSV na pasta `csv_files`.
5. Um arquivo ZIP contendo o arquivo CSV/PDF será criado na pasta `zip_files`.

Certifique-se de criar as sub pastas para as etapas de Web Scraping e Transformação de Dados antes de executar o script.




## Etapa 3: Análise de Demonstrativos Contábeis de Operadoras de Saúde

Esta etapa do projeto visa analisar os demonstrativos contábeis das operadoras de saúde para identificar as 10 operadoras com maiores despesas em geral e nas categorias específicas nos últimos anos. Ele inclui a estruturação das tabelas necessárias no banco de dados e a importação de dados de arquivos CSV preparados, seguidos pela execução de consultas SQL para extrair informações relevantes.

### Requisitos

- MySQL
- Linguagem SQL
- Ambiente de desenvolvimento com suporte para execução de consultas SQL

### Estrutura e Importação de dados da Tabela

Para executar as consultas SQL, é necessário criar uma conexão com o banco de dados no MySQL, além de executar os comandos de CREATE TABLE e LOAD DATA INFILE apresentados no arquivo `estrutura_banco.sql`



## Etapa 4: Servidor da API Flask

Esta etapa é um servidor Flask que fornece uma rota para realizar buscas textuais em uma lista de cadastros de operadoras de planos de saúde.

### Pré-requisitos

Certifique-se de ter o Python e o Flask instalados em sua máquina.

### Uso
1. Certifique-se de ter o arquivo CSV com os dados das operadoras de planos de saúde no diretório correto.
2. Execute o servidor Flask:



## Etapa 5: Análise de Demonstrativos Contábeis de Operadoras de Saúde

Esta etapa do projeto demonstra como criar uma interface de busca usando Flask para o backend e Vue.js para o frontend.

### Pré-requisitos

Certifique-se de ter o Node.js e o npm instalados em sua máquina.

### Uso
1. Insira o termo de busca e o nome da coluna de busca nos campos de entrada.
2. Clique no botão "Search" para enviar a busca.
3. Os resultados da busca serão exibidos abaixo dos campos de entrada.




## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE.md para mais detalhes.