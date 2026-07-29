import  sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES(?,?)", (nome,id_turma))
        conexao.commit()

    except ValueError:
        # Captura quando o usuário digita letras no lugar do número
        print("Erro: Você deve digitar apenas números para o ID da turma!")
    except sqlite3.Error:
        print("Erro no banco de dados!")
    finally:
        if 'conexao' in locals():
            conexao.close()
       
# o except sqlite3.Error: análisava erros do sqlite, para ele poder detectar erro no ID precisar por o erro do valor se digita-se no ID "turma b".
vincular_aluno_turma()