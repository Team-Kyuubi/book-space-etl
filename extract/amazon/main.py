from urls import biografias
from urls import ciencias
from urls import desenvolvimento_pessoal
from urls import economia
from urls import ficcao_cientifica
from urls import negocios
from urls import romances
from urls import tecnologia
from urls import terror
from scraping_padrao import scraping_padrao
from scraping_terror import scraping_terror

categorias = [
    biografias.categoria, ciencias.categoria, desenvolvimento_pessoal.categoria, economia.categoria,
    ficcao_cientifica.categoria, negocios.categoria, romances.categoria, tecnologia.categoria, terror.categoria
]
links = [
    biografias.url_livros, ciencias.url_livros, desenvolvimento_pessoal.url_livros, economia.url_livros,
    ficcao_cientifica.url_livros, negocios.url_livros, romances.url_livros, tecnologia.url_livros, terror.url_livros
]

cont = 0
while cont < len(categorias):
    if categorias[cont] == 'Terror':
        scraping_terror()
    else:
        scraping_padrao(links[cont], categorias[cont])
    cont = cont + 1
