import TransformacaoDeDados.transformacao_dados as transformacao_dados
import WebScraping.web_scraping as web_scraping

def main():
    # Executar a extração e transformação de dados
    transformacao_dados.main()

    # Executar o web scraping e download dos arquivos
    web_scraping.main()

if __name__ == "__main__":
    main()
