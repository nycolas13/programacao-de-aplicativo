from banco import connect

def cadastrar_turmas(nome_turma, id_escola):
    assert nome_turma.strip() != "", "O nome da turma não pode ser vazio."
    assert id_escola > 0, "O ID da escola deve ser maior que zero."

    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO turmas( nome_turma, id_escola) VALUES (?, ?)",(nome_turma, id_escola))
    conexao.commit()
    conexao.close()

def listar_turmas():
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM turmas")
    turmas = cursor.fetchall()
    conexao.close()
    return turmas