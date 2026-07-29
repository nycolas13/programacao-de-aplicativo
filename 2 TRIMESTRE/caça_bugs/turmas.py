import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreing_key = ON;")

    cursor.execute("INSERT INTO turmas(nome_turma, id_serie, id_professor) VALUES (?,?, ?)",(nome, id_serie, id_prof))
    conexao.commit()
    conexao.close()

# a linha conexao.close() não fechara 