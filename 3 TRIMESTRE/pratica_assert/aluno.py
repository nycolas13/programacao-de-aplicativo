from banco import connect

def cadastrar_alunos(nome, idade, id_turma):
    assert nome.strip() != "", "O nome do aluno não pode ser vazio."
    assert idade >= 3, "A idade mínima do aluno deve ser 3 anos."
    assert id_turma > 0, "O ID da turma deve ser maior que zero."

    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos(nome, idade, id_turma) VALUES (?,?,?)", (nome, idade, id_turma))
    conexao.commit()
    conexao.close()

def listar_aluno():
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()
    return alunos