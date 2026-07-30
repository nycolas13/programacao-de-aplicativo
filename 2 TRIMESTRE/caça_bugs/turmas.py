import sqlite3

nome = input("Digite seu nome: ")
id_serie = int(input("Digite o ID da série: "))
id_prof = int(input("Digite o ID do seu professor: "))

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            id_serie INTEGER,
            id_prof INTEGER)
            ''')
    cursor.execute("PRAGMA foreing_key = ON;")

    cursor.execute("INSERT INTO turmas(nome, id_serie, id_prof) VALUES (?,?, ?)",(nome, id_serie, id_prof))
    conexao.commit()
    conexao.close()

# a linha conexao.close() não fechara 
# Tava dando erro porque o banco turmas não existia existia na tabela e os argumentos não estavam posicionados.
cadastrar_turma(nome, id_serie, id_prof)