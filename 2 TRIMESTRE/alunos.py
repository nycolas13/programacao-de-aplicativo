import  sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    id_turma = int(input("Digite o ID numérico da turma: "))

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES(?,?)", (nome,id_turma))

    conexao.commit()
    print("Erro no banco de dados!")
    conexao.close()

# falta CREATE TABLE