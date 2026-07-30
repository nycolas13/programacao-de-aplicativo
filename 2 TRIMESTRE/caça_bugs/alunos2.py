import sqlite3 

novo_nome = input("Digite o nome: ")
id_aluno = int(input("Digite o ID: "))

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS aluno(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            )
        ''')

    cursor.execute("UPDATE aluno SET nome = ? WHERE id = ?", (novo_nome, id_aluno))
    
    conexao.commit()
    conexao.close()

# Estava faltando o "WHERE", a tabela e o banco "aluno" que estava escrito "alunos" (que já existe) 
atualizar_nome_aluno(3, "Novo Nome do Aluno")