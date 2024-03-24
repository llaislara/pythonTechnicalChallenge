import os
import csv  
from zipfile import ZipFile
import pdfplumber
import pandas as pd
import re

pdf_file_path = './WebScraping/pdf_files/Anexo_1.pdf'

# Função para extrair os dados da tabela
def extract_table_data(pdf_file_path):
    table_data = []
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            in_table = False
            for line in lines:
                if 'PROCEDIMENTO' in line:
                    in_table = True
                    continue
                if 'Total' in line:
                    in_table = False
                    break
                if in_table:
                    row_data = re.split(r'\s{2,}', line.strip())
                    table_data.append(row_data)
    return table_data

table_data = extract_table_data(pdf_file_path)

# Salva os dados em um arquivo CSV
csv_file_path = './TransformacaoDeDados/csv_files/dados_extraidos.csv' 
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in table_data:
        writer.writerow(row)

print("Dados extraídos salvos em", csv_file_path)

# Compacta o arquivo CSV em um arquivo ZIP
zip_file_path = './TransformacaoDeDados/zip_files/dados_extraidos.zip'  
with ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(csv_file_path, os.path.basename(csv_file_path))

print("Arquivo ZIP criado com sucesso:", zip_file_path)
