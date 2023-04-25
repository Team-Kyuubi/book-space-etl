from urls import biografias
from urls import romances
from urls import tecnologia
from urls import ficcao_cientifica
from scraping_biografias import scraping_biografias
from scraping_padrao import scraping_padrao

categorias = [biografias.categoria, ficcao_cientifica.categoria, romances.categoria, tecnologia.categoria]
links = [biografias.url_livros, ficcao_cientifica.url_livros, romances.url_livros, tecnologia.url_livros]

cont = 0
while(cont < len(categorias)):
    if categorias[cont] == 'Biografia':
        scraping_biografias()
    else:
        scraping_padrao(links[cont], categorias[cont])
    cont = cont + 1
