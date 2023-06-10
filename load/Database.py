import mysql.connector as mysql


class DataBase:
    host = "127.0.0.1"
    user = "root"
    password = "2592"
    database = "bookspace"

    def conectar_ao_banco_de_dados(self):
        return mysql.connect(host=self.host, user=self.user, database=self.database, password=self.password)

    def inserir_autor(self, nome_autor):
        con = self.conectar_ao_banco_de_dados()
        cursor = con.cursor()
        cursor.execute("INSERT INTO autor_livro (nome_autor) VALUES (%s);", (nome_autor,))
        con.commit()
        con.close()

    def inserir_idioma(self, idioma):
        con = self.conectar_ao_banco_de_dados()
        cursor = con.cursor()
        cursor.execute("INSERT INTO idioma_livro (idioma) VALUES (%s)", (idioma,))
        con.commit()
        con.close()

    def inserir_genero(self, genero):
        con = self.conectar_ao_banco_de_dados()
        cursor = con.cursor()
        cursor.execute("INSERT INTO genero_livro (genero) VALUES (%s);", (genero,))
        con.commit()
        con.close()

    def inserir_editora(self, editora):
        con = self.conectar_ao_banco_de_dados()
        cursor = con.cursor()
        cursor.execute("INSERT INTO editora_livro (nome_editora) VALUES (%s);", (editora,))
        con.commit()
        con.close()

    def inserir_livro(self, nome_livro, valor, paginas, descricao, link_img, id_autor, id_genero, id_editora, id_idioma):
        con = self.conectar_ao_banco_de_dados()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO livro (nome_livro, valor, numero_paginas, descricao, url_imagem, id_autor, id_genero, "
            "id_editora, id_idioma) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
            (nome_livro, valor, paginas, descricao, link_img, id_autor, id_genero, id_editora, id_idioma)
        )
        con.commit()
        cursor.close()

    def inserir_livros(self, dataframe):
        cont = 0
        while cont < dataframe.shape[0]:
            self.inserir_livro(
                dataframe.loc[cont]['titulo'], str(dataframe.loc[cont]['preco']),
                str(dataframe.loc[cont]['paginas']),
                dataframe.loc[cont]['descricao'], dataframe.loc[cont]['img_link'], str(dataframe.loc[cont]['id_autor']),
                str(dataframe.loc[cont]['id_genero']), str(dataframe.loc[cont]['id_editora']),
                str(dataframe.loc[cont]['id_idioma'])
            )
            cont = cont + 1

    def inserir_dados(self, dataframe, coluna):
        cont = 0
        while cont < dataframe.shape[0]:
            info = dataframe.loc[cont][coluna]
            if coluna == 'autor':
                self.inserir_autor(info)
            elif coluna == 'idioma':
                self.inserir_idioma(info)
            elif coluna == 'genero':
                self.inserir_genero(info)
            elif coluna == 'editora':
                self.inserir_editora(info)
            cont = cont + 1
