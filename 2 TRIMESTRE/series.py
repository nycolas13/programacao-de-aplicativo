import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO series(nome_serie, id_escola) VALUES(?,?)",(nome_serie, id_escola))
    conexao.commit()
    
    print("Erro: Escola inexistente!")
    conexao.close()
    # O erro é ciar a tabela "CREATE TABLE" 
    