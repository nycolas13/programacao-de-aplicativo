import sqlite3

def criar_cinemas(id_pk, nome_cinema, shopping):
    conexao = sqlite3.connect('pai_hospitais.db')
    cursor = conexao.cursor()

    cursor.execute(''')