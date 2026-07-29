import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS escolas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT
                   )
                   ''')
    
    cursor.execute('''
                 CREATE TABLE IF NOT EXISTS series(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_serie TEXT,
                   id_escola INTERGER,
                   FOREIGN KEY (id_escola)  REFERENCES escolas(id)
                   )  
                   ''')
    conexao.commit()
    conexao.close()

    criar_tabelas()

 # O erro era que a tabela series tentava criar uma chave estrangeira para a tabela escolas (que ainda não existia), então troca-se a ordem 
 # colocando a tabela escolas primeiro e a tabela da series em segudo, assim a tabela escolas existe, podemdo assim a tabela series criar uma cheve estrangeira para escolas.











   