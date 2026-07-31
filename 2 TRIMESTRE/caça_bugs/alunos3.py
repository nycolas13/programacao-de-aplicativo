import sqlite3

def verificar_registro():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    print("Primeiro print:", alunos)
    print("Segundo print:", alunos)

    conexao.close()

# O cursor.fetchall() funciona como um "leitor de fita" — uma vez que ele lê todos os dados, chega ao fim. Para reutilizar os dados, guarde-os em uma variável(alunos = cursor.fetchall())!
verificar_registro()