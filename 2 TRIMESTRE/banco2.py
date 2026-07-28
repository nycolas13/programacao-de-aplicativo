import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS series(
                   id INTERGER PRIMARY KEY AUTOINCREMENT,
                   nome_serie TEXT,
                   id_escola INTERGER,
                   FOREIGN KEY (id_escola)  REFERENCES escolas(id)
                   )
                   ''')
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS escolas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT
                   )
                   ''')
    conexao.commit()
    conexao.close()

    # O erro do primeiro bloco é a chave estrangeira(FOREING KEY), porque quando o bloco vai rodar pela primeura vez, não tem nescessidade de trazer 
    # chaves estrangeiras.