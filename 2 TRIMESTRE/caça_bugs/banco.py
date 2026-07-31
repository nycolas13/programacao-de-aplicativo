import sqlite3
import os

def inicializar_banco():
    # Garante que o arquivo .db seja criado na MESMA pasta deste script .py
    caminho_banco = os.path.join(os.path.dirname(__file__), 'sistema_escola.db')
    
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    
    conexao.commit()
    conexao.close()
    print(f"Banco inicializado com sucesso em: {caminho_banco}")

# Executa a função
# Falta do commit()
inicializar_banco()