import sqlite3

nome_serie = input("Digite o nome da serie: ")
id_escola = int(input("Digite seu ID: "))

def cadastrar_serie(nome_serie, id_escola):
    conexao = None
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO serie (nome_serie, id_escola) VALUES(?, ?)",(nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: A escola com este ID não existe no banco de dados!")
        
    except ValueError:
        print("Erro: O ID deve ser um número inteiro válido.")
        
    except sqlite3.Error as e:
        print("Erro no banco de dados:", e)
    finally:
        if conexao:
            conexao.close()

cadastrar_serie(nome_serie, id_escola)