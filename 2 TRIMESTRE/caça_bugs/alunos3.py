import sqlite3

def verificar_registro():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    print("Primeiro print:", cursor.fetchall())
    print("Segundo print:", cursor.fetchall())

    conexao.close()