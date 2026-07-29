import sqlite3

nome_serie = input("Digite o nome da serie: ")
id_escola = int(input("Digite seu ID: "))

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    try:
        cursor.execute("INSERT INTO serie (nome_serie, id_escola) VALUES(?, ?)",(nome_serie, id_escola))
        conexao.commit()
    except sqlite3.integrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()

cadastrar_serie(nome_serie, id_escola)