import sqlite3

nome = input("Digite o nome: ")
cpf = int(input("Digite o CPF: "))

def cadastar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT UNIQUE
        )
        ''')
    
# Para evitar de cadastrar dois professores com o mesmo CPF, na tabela coloque "UNIQUE", o que ajuda a torna o cpf de um professor unica.
# Evitando da cadastrar dois professores com o mesmo CPF.
    
cadastar_professor(nome, cpf)