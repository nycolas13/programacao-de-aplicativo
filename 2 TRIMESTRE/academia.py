import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect('pai_hospital.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS academia(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_unidade TEXT,
            bairro TEXT)''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            mensali INTEGER NOT NULL,
            id_academia INTEGER NOT NULL,
            FOREIGN KEY (id_academia) REFERENCES academia (id)
            )''')