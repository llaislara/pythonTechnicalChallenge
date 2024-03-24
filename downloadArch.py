import requests
from datetime import datetime

# URL base para os arquivos de demonstrações contábeis
base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

# Obter o ano anterior
ano_atual = datetime.now().year
ano_anterior = ano_atual - 1

# Baixar os arquivos dos últimos 2 anos
for ano in range(ano_anterior - 1, ano_atual):
    url = f"{base_url}{ano}/"
    response = requests.get(url)
    if response.status_code == 200:
        files = response.text.splitlines()
        for file in files:
            if file.endswith('.zip'):
                filename = file.split("/")[-1]
                with open(filename, 'wb') as f:
                    f.write(requests.get(file).content)
                    print(f"Arquivo {filename} baixado com sucesso.")
    else:
        print(f"Erro ao acessar {url}: {response.status_code}")


# URL para os dados cadastrais das operadoras ativas na ANS em formato CSV
url_operadoras = "https://dados.gov.br/dados/conjuntos-dados/operadoras-de-planos-privados-de-saude"

# Nome do arquivo de saída
nome_arquivo_csv = "operadoras_ativas_ans.csv"

# Realizar a solicitação HTTP para obter o conteúdo do arquivo CSV
response = requests.get(url_operadoras)

# Verificar se a solicitação foi bem sucedida
if response.status_code == 200:
    # Salvar o conteúdo do arquivo CSV em um arquivo local
    with open(nome_arquivo_csv, 'wb') as f:
        f.write(response.content)
    print(f"Arquivo {nome_arquivo_csv} baixado com sucesso.")
else:
    print(f"Erro ao acessar {url_operadoras}: {response.status_code}")
