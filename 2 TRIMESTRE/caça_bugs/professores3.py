import sqlite3

nome = input("Digite o nome: ")
materia = input("Digite a matéria: ")
cpf = int(input("Digite o CPF: "))

def inserir_professor(nome, materia, cpf):
    conexao = None
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf))
        conexao.commit()
    except sqlite3.Error:
        print("Erro: Este CPF já está cadastrado no sistema!")
    finally:
        conexao.close()

# Erro "INSERTO" o correto é INSERT.
inserir_professor(nome, materia, cpf)