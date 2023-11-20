import pandas as pd
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://application:25923389@cluster0.5rmhnzg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
database = client['dev']
collection = database['book']


def inserir_livro(livro):
    collection.insert_one(livro)


df = pd.read_json('D:/Projects/Book Space/book-space-etl/transform/amazon/resultado/livros.json')

cont = 0
while cont < df.shape[0]:
    linha = df.iloc[cont]
    generos = linha.generos.split(' | ')
    livro = {
        'isbn13': linha.isbn13,
        'isbn10': linha.isbn10,
        'bookName': linha.titulo,
        'pages': int(linha.paginas),
        'description': linha.idioma,
        'imageUrl': linha.editora,
        'authors': [
            linha.autor
        ],
        'gender': generos,
        'publisher': linha.editora,
        'idiom': linha.idioma,
        'amazonLink': linha.amazonLink
    }
    inserir_livro(livro)
    cont = cont + 1
