import requests
import os
from bs4 import BeautifulSoup
from zipfile import ZipFile

if not os.path.exists("pdf_files"):
    os.makedirs("pdf_files")
if not os.path.exists("zip_files"):
    os.makedirs("zip_files")

# 1.1 Acesso ao site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 1.2 Identificação e download dos Anexos I e II em formato PDF
pdf_links = []
for link in soup.find_all("a", href=True):
    if link["href"].endswith(".pdf") and ("Anexo I" in link.text or "Anexo II" in link.text):
        pdf_links.append(link["href"])

# 1.3 Download dos PDFs sem compactação
for index, pdf_link in enumerate(pdf_links, start=1):
    pdf_data = requests.get(pdf_link).content
    file_name = f"WebScraping/pdf_files/Anexo_{index}.pdf" 
    with open(file_name, "wb") as pdf_file:
        pdf_file.write(pdf_data)
    print(f"Arquivo {file_name} baixado com sucesso.")

# 1.2 Download dos links formato PDF para compactação
pdf_links = [link["href"] for link in soup.find_all("a", href=True) if link["href"].endswith(".pdf")]

# 1.3 Compactação de todos os anexos em um único arquivo
with ZipFile("WebScraping/zip_files/anexos.zip", "w") as zipf:  
    for pdf_link in pdf_links:
        pdf_data = requests.get(pdf_link).content
        file_name = pdf_link.split("/")[-1]
        zipf.writestr(file_name, pdf_data)

print("Downloads concluídos e arquivos compactados com sucesso.")
