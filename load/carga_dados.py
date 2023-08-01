import json
from pymongo.mongo_client import MongoClient

uri = "mongodb://localhost:27017"
client = MongoClient(uri)
database = client['bookspace']
collection = database['book']

json_file = open('D:/Projects/Book Space/book-space-etl/transform/resultado/livros.json')

data = json.load(json_file)


def inserir_livro(livro):
    collection.insert_one(livro)


cont = 0
while cont < 89:
    livro = {
        'isbn_13': data['isbn_13'][f'{cont}'],
        'isbn_10': data['isbn_10'][f'{cont}'],
        'book_name': data['titulo'][f'{cont}'],
        'pages': data['paginas'][f'{cont}'],
        'description': data['descricao'][f'{cont}'],
        'image_url': data['img_link'][f'{cont}'],
        'authors': {
            'author_1': data['autor'][f'{cont}']
        },
        'gender': {
            'gender_1': data['genero'][f'{cont}']
        },
        'publisher': data['editora'][f'{cont}'],
        'idiom': data['idioma'][f'{cont}']
    }
    inserir_livro(livro)
    cont = cont + 1
