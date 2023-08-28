from urls import terror

import pandas as pd
from Scraper import Scraper


def scraping_terror():
    scraper = Scraper()

    livros = {
        'titulo': [],
        'descricao': [],
        'paginas': [],
        'idioma': [],
        'editora': [],
        'autor': [],
        'genero': [],
        'imgLink': [],
        'isbn13': [],
        'isbn10': [],
        'amazonLink': []
    }

    cont = 0
    for url in terror.url_livros:
        scraper.iniciar_busca(url)

        titulo = scraper.busca_por_id('productTitle')
        livros['titulo'].append(titulo)

        if cont == 1 or cont == 4:
            descricao = scraper.busca_por_xpath('//*[@id="bookDescription_feature_div"]/div/div[1]/p')
        elif cont == 6:
            descricao = scraper.busca_por_xpath('//*[@id="bookDescription_feature_div"]/div/div[1]/span')
        else:
            descricao = scraper.busca_por_xpath('//*[@id="bookDescription_feature_div"]/div/div[1]')
        livros['descricao'].append(descricao)

        paginas = scraper.busca_por_xpath('//*[@id="rpi-attribute-book_details-fiona_pages"]/div[3]/span')
        livros['paginas'].append(paginas)

        idioma = scraper.busca_por_xpath('//*[@id="rpi-attribute-language"]/div[3]/span')
        livros['idioma'].append(idioma)

        editora = scraper.busca_por_xpath('//*[@id="rpi-attribute-book_details-publisher"]/div[3]/span')
        livros['editora'].append(editora)

        autor = scraper.busca_por_xpath('//*[@id="bylineInfo"]/span[1]/a')
        livros['autor'].append(autor)

        livros['genero'].append(terror.categoria)

        img_link = scraper.buscar_src_imagem('imgBlkFront')
        livros['imgLink'].append(img_link)

        isbn = scrap_isbn(scraper)
        livros['isbn10'].append(isbn[0])
        livros['isbn13'].append(isbn[1])

        livros['amazonLink'].append(url)

        cont = cont + 1

    scraper.finalizar_busca()

    livros = pd.DataFrame(data=livros)
    livros.to_csv('D:/Projects/Book Space/book-space-etl/extract/extracoes/Terror.csv')


def scrap_isbn(scraper):
    isbn_10 = scraper.busca_isbn('//*[@id="rpi-attribute-book_details-isbn10"]/div[3]')
    isbn_13 = scraper.busca_isbn('//*[@id="rpi-attribute-book_details-isbn13"]/div[3]')
    return isbn_10, isbn_13
