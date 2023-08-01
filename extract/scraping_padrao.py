import pandas as pd
from Scraper import Scraper


def scraping_padrao(links, categoria):
    scraper = Scraper()

    livros = {
        'titulo': [],
        'descricao': [],
        'paginas': [],
        'idioma': [],
        'editora': [],
        'autor': [],
        'genero': [],
        'img_link': [],
        'isbn_13': [],
        'isbn_10': []
    }

    for url in links:
        print(url)
        scraper.iniciar_busca(url)

        titulo = scraper.busca_por_id('productTitle')
        livros['titulo'].append(titulo)

        if url == "https://www.amazon.com.br/Regresso-Peregrino-aleg%C3%B3rica-cristianismo-romantismo/dp/6556893811" \
                  "/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=&sr=1-1":
            descricao = scraper.busca_por_xpath('// *[ @ id = "bookDescription_feature_div"] / div / div[1] / span[1]')
        else:
            descricao = scraper.busca_por_xpath('//*[@id="bookDescription_feature_div"]/div/div[1]')
        livros['descricao'].append(descricao)

        paginas = scraper.busca_por_xpath('//*[@id="rpi-attribute-book_details-fiona_pages"]/div[3]/span')
        livros['paginas'].append(paginas)

        idioma = scraper.busca_por_xpath('//*[@id="rpi-attribute-language"]/div[3]/span')
        livros['idioma'].append(idioma)

        editora = scraper.busca_por_xpath('//*[@id="rpi-attribute-book_details-publisher"]/div[3]/span')
        print(editora)
        livros['editora'].append(editora)

        autor = scraper.busca_por_xpath('//*[@id="bylineInfo"]/span[1]/a')
        livros['autor'].append(autor)

        livros['genero'].append(categoria)

        img_link = scraper.buscar_src_imagem('imgBlkFront')
        livros['img_link'].append(img_link)

        isbn = scrap_isbn(scraper)
        livros['isbn_10'].append(isbn[0])
        livros['isbn_13'].append(isbn[1])

        # print(f"ISBN10: {isbn[0]}")
        # print(f"ISBN13: {isbn[1]}")

    scraper.finalizar_busca()

    livros = pd.DataFrame(data=livros)
    livros.to_csv(f'D:/Projects/Book Space/book-space-etl/extract/extracoes/{categoria}.csv')


def scrap_isbn(scraper):
    isbn_10 = scraper.busca_isbn('//*[@id="rpi-attribute-book_details-isbn10"]/div[3]')
    isbn_13 = scraper.busca_isbn('//*[@id="rpi-attribute-book_details-isbn13"]/div[3]')
    return isbn_10, isbn_13
