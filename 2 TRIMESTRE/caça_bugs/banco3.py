import sqlite3

nome = input("Digite um nome: ")

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def inserir_escola(nome):
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()

inserir_escola(nome)
# Quando usa múltiplos arquivos (módulos) no Python e faz um import de outro arquivo, o Python executa imediatamente todo o código que está fora das funções.