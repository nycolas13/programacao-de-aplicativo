import sqlite3

def cadastrar_lista_alunos():

    lista = [("ANA", 1), ("Carlos",1), ("Beatriz",2)]

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            id_turma INTEGER
        )
    ''')
 
    lista = [("ANA", 1), ("Carlos",1), ("Beatriz",2)]
  

    cursor.executemany("INSERT INTO alunos (nome, id_turma) VALUES (?,?)", lista)

    conexao.commit()
    conexao.close()
    print("Tabela verificada e alunos cadastrados com sucesso!")

# O execute ele serve para inserir um único registro de cada vez
# Mas o executemany é feito para inserir uma lista inteira de tuplas.
# Tem erro A tabela alunos não possui uma coluna chamada nome.


cadastrar_lista_alunos()