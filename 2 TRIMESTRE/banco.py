import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS escolas (
                id INTERGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
                )''')
    conexao.commit()
    conexao.close()
    # Faltou o conexao.commit, que é justamente o comando para salvar.
inicializar_banco()