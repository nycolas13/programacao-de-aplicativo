import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    # Lista simples com as tabelas permitidas
    tabelas_validas = ["alunos", "professores", "turmas", "series"]
    
    # 1. Se a tabela não for válida, cancela na hora
    if nome_tabela not in tabelas_validas:
        print("Tabela inválida!")
        return

    # 2. Conecta e busca de forma simples usando 'with'
    with sqlite3.connect('sistema_escola.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id = ?", (id_registro,))
        print(cursor.fetchone())

buscar_dados_dinamicos(nome_tabela= "alunos", id_registro=1)