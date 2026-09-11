def buscar_aluno_por_nome(conexao):
    cursor = conexao.cursor()
    
    # Recebe o nome digitado pelo usuário
    nome_procurado = input("Digite o nome do aluno que deseja buscar: ")
    
    # Utiliza LIKE para encontrar correspondências (parciais ou totais) ordenadas
    sql = "SELECT * FROM alunos WHERE nome LIKE ? ORDER BY nome ASC"
    
    # O '%' permite buscar partes do nome; o parâmetro evita SQL Injection
    cursor.execute(sql, ('%' + nome_procurado + '%',))
    alunos = cursor.fetchall()
    
    for aluno in alunos:
        print(aluno)