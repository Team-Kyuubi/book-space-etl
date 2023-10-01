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
        'imgLink': [],
        'isbn13': [],
        'isbn10': [],
        'amazonLink': []
    }

    for url in links:
        scraper.iniciar_busca(url)

        titulo = scraper.busca_por_xpath('//*[@id="productTitle"]')
        livros['titulo'].append(titulo)

        if url == "https://www.amazon.com.br/Regresso-Peregrino-aleg%C3%B3rica-cristianismo-romantismo/dp/6556893811" \
                  "/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=&sr=1-1":
            descricao = scraper.busca_por_xpath('// *[ @ id = "bookDescription_feature_div"] / div / div[1] / span[1]')
        else:
            descricao = scraper.busca_por_xpath('//*[@id="bookDescription_feature_div"]/div/div[1]')
        livros['descricao'].append(descricao)

        paginas = scraper.busca_por_xpath('//*[@id="detailBullets_feature_div"]/ul/li[3]/span/span[2]')
        livros['paginas'].append(paginas)

        idioma = scraper.busca_por_xpath('//*[@id="detailBullets_feature_div"]/ul/li[2]/span/span[2]')
        livros['idioma'].append(idioma)

        editora = scraper.busca_por_xpath('//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]')
        livros['editora'].append(editora)

        autor = scraper.busca_por_xpath('//*[@id="bylineInfo"]/span[1]/a')
        livros['autor'].append(autor)

        livros['genero'].append(categoria)

        img_link = scraper.buscar_src_imagem('landingImage')
        livros['imgLink'].append(img_link)

        isbn = scrap_isbn(scraper, url)
        livros['isbn10'].append(isbn[0])
        livros['isbn13'].append(isbn[1])

        livros['amazonLink'].append(url)

    scraper.finalizar_busca()

    livros = pd.DataFrame(data=livros)
    livros.to_csv(f'D:/Projects/Book Space/book-space-etl/extract/extracoes/{categoria}.csv')


def scrap_isbn(scraper, url):
    isbn_10 = scraper.buscar_isbn('//*[@id="detailBullets_feature_div"]/ul/li[4]/span/span[2]')
    if url == 'https://www.amazon.com.br/As-coisas-que-homens-explicam/dp/9897222952/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3' \
              '%85%C5%BD%C3%95%C3%91&keywords=Os+Homens+Me+Explicam+Coisas&sr=8-1':
        isbn_13 = scraper.buscar_isbn('// *[ @ id = "detailBullets_feature_div"] / ul / li[4] / span / span[2]')
    else:
        isbn_13 = scraper.buscar_isbn('//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[2]')

    return isbn_10, isbn_13
