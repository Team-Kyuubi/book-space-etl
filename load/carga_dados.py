import json
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://application:25923389@cluster0.5rmhnzg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
database = client['dev']
collection = database['book']

json_file = open('D:/Projects/Book Space/book-space-etl/transform/resultado/livros.json')

data = json.load(json_file)


def inserir_livro(livro):
    collection.insert_one(livro)


cont = 0
while cont < 89:
    livro = {
        'isbn13': data['isbn13'][f'{cont}'],
        'isbn10': data['isbn10'][f'{cont}'],
        'bookName': data['titulo'][f'{cont}'],
        'pages': data['paginas'][f'{cont}'],
        'description': data['descricao'][f'{cont}'],
        'imageUrl': data['imgLink'][f'{cont}'],
        'authors': [
            data['autor'][f'{cont}']
        ],
        'gender': [
            data['genero'][f'{cont}']
        ],
        'publisher': data['editora'][f'{cont}'],
        'idiom': data['idioma'][f'{cont}'],
        'amazonLink': data['amazonLink'][f'{cont}']
    }
    inserir_livro(livro)
    cont = cont + 1
