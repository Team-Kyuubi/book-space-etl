from Database import DataBase
import pandas as pd

db = DataBase()

df = pd.read_csv('../transform/resultado/livros.csv')

tabelas = ['autor', 'idioma', 'genero', 'editora']
for tabela in tabelas:
    info = pd.DataFrame(df[tabela].unique())
    info.columns = [tabela]
    db.inserir_dados(info, tabela)

db.inserir_livros(df)
