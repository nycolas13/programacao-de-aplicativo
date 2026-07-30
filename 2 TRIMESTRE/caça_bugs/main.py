import sqlite3

def listar_alunos_e_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas ON alunos.id_turma = turmas.id")

    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
    conexao.close()

# o ERRO era a falta do ON que compara a chave estrangeira da tabela alunos com a chave primária da tabela turmas e traz só as combinações corretas.
listar_alunos_e_turma()