from urls import terror

import pandas as pd
from Scraper import Scraper


def scraping_terror():
    scraper = Scraper()

    livros = {
        'titulo': [],
        'preco': [],
        'descricao': [],
        'paginas': [],
        'idioma': [],
        'editora': [],
        'autor': [],
        'genero': [],
        'img_link': []
    }

    cont = 0
    for url in terror.url_livros:
        scraper.iniciar_busca(url)

        titulo = scraper.busca_por_id('productTitle')
        livros['titulo'].append(titulo)

        preco = scraper.busca_por_id('kindle-price')
        livros['preco'].append(preco)

        if cont == 1 or cont == 4 or cont == 6:
            descricao = scraper.busca_por_xpath('//*[@id="bookDescription_feature_div"]/div/div[1]/p')
        else:
            descricao = scraper.busca_por_xpath('//*[@id="bookDescription_feature_div"]/div/div[1]')
        livros['descricao'].append(descricao)

        paginas = scraper.busca_por_xpath('//*[@id="rpi-attribute-book_details-ebook_pages"]/div[3]/span/a/span')
        livros['paginas'].append(paginas)

        idioma = scraper.busca_por_xpath('//*[@id="rpi-attribute-language"]/div[3]/span')
        livros['idioma'].append(idioma)

        editora = scraper.busca_por_xpath('//*[@id="detailBullets_feature_div"]/ul/li[2]/span/span[2]')
        livros['editora'].append(editora)

        autor = scraper.busca_por_xpath('//*[@id="bylineInfo"]/span[1]/a')
        livros['autor'].append(autor)

        livros['genero'].append(terror.categoria)

        img_link = scraper.buscar_src_imagem('ebooksImgBlkFront')
        livros['img_link'].append(img_link)

        cont = cont + 1

    scraper.finalizar_busca()

    livros = pd.DataFrame(data=livros)
    livros.to_csv('extracoes/Terror.csv')
