from urls import biografias
from urls import ciencias
from urls import ficcao_cientifica
from urls import romances
from urls import tecnologia
from urls import terror
from scraping_biografias import scraping_biografias
from scraping_padrao import scraping_padrao
from scraping_terror import scraping_terror

categorias = [biografias.categoria, ciencias.categoria, ficcao_cientifica.categoria, romances.categoria, tecnologia.categoria, terror.categoria]
links = [biografias.url_livros, ciencias.url_livros, ficcao_cientifica.url_livros, romances.url_livros, tecnologia.url_livros, terror.url_livros]

cont = 0
while(cont < len(categorias)):
    if categorias[cont] == 'Biografia':
        scraping_biografias()
    elif categorias[cont] == 'Terror':
        scraping_terror()
    else:
        scraping_padrao(links[cont], categorias[cont])
    cont = cont + 1
