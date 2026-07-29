import sqlite3

def cadastrar_escola_manual():
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('istema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO escolas (id, nome) VALUES (?,?)", (id_escola, nome))

    conexao.commit()
    conexao.close()