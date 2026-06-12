import sqlite3
def cadastrar_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    print("Conectando ao banco de dados........")
    print("---SISTEMA DE CADASTRO---")

    # Criando tabela
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS aluno(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL
                    )''')

    print("Tabela e configurações")
    nome_aluno = input("Nome Completo: ")
    telefone_aluno = input("Tel: ")
    turma_aluno = input("Classificação de turma: ")
    idade_aluno = int(input("Idade do Aluno: "))
    cpf_aluno = input("CPF do aluno: ")

    comando_inserir = f'''
                        INSERT INTO aluno(
                            nome,
                            telefone,
                            turma,
                            idade,
                            cpf
                            )
                        VALUES (
                            '{nome_aluno}', 
                            '{telefone_aluno}', 
                            '{turma_aluno}',
                            '{idade_aluno}',
                            '{cpf_aluno}'
                            )'''

    cursor.execute(comando_inserir)

    conexao.commit()
    conexao.close()

    print("Aluno cadastrado com sucesso!")


def listar_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno")
    resultados = cursor.fetchall()

    print("   DADOS DOS ALUNOS CADASTRADOS   ")

    for aluno in resultados:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Tel: {aluno[2]} | Turma: {aluno[3]} | Idade: {aluno[4]} | CPF: {aluno[5]}")
        print("-" * 30)
    # 5. Fecha a conexão
    conexao.close()
    print("  DESLIGANDO SISTEMA......")


def alterar_dados_aluno():
    print("Conectando ao banco de dados........")
    print("\n--- ATUALIZAÇÃO DE CADASTRO ---")
    print("Bem-vindo de volta. O que quer fazer hoje?")
    id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
    novo_nome = input("Digite o NOVO nome completo: ")
    novo_cpf = input("Digite o NOVO CPF: ")

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    sql_update = """
    UPDATE aluno
    SET nome = ?,
    cpf = ?
    WHERE id = ?
    """
    cursor.execute(sql_update, (novo_nome, novo_cpf, id_aluno))
    
    # 2. Passa as variáveis do input para dentro da função
    conexao.commit()
    conexao.close()
    print("Aluno atualizado com sucesso!")
    print("  DESLIGANDO SISTEMA......")

def excluir_aluno():
    print("Conectando ao banco de dados........")
    print("Bem-vindo de volta. O que quer fazer hoje?")
    print("---SISTEMA DE EXCLUSÃO DE ALUNOS---")
    id_aluno = int(input("Digite o ID do aluno que deseja EXCLUIR: "))
    
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    sql_delete = """
    DELETE FROM aluno
    WHERE id = ?
    """

    print("Aluno EXCLUIDO COM SUCESSO")
    print("  DESLIGANDO SISTEMA......")

    cursor.execute(sql_delete,(id_aluno,))
    conexao.commit()
    conexao.close()


cadastrar_aluno()
listar_aluno()
alterar_dados_aluno()
excluir_aluno()


