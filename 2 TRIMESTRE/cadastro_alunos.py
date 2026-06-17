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

def cadastrar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    print("Abrindo arquivo.....")
    print("---CADASTRO de PROFESSORES---")


    nome_prof = input("NOME: ")
    telefone_prof = input("TELEFONE: ")
    materia_prof = input("MATÉRIAS: ")
    idade_prof = int(input("IDADE: "))
    cpf_prof = input("CPF: ")
    salario_prof = float(input("SALÁRIO: "))
    escola_prof = input("Nome da Escola: ")

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    salario REAL,
                    escola TEXT
                    )''')

    comando_inserir = f'''
                    INSERT INTO professores(
                        nome,
                        telefone,
                        materia,
                        idade,
                        cpf,
                        salario,
                        escola
                        )
                    VALUES (
                        '{nome_prof}',
                        '{telefone_prof}',
                        '{materia_prof}',
                        '{idade_prof}',
                        '{cpf_prof}',
                        '{salario_prof}',
                        '{escola_prof}'
                        )'''

    cursor.execute(comando_inserir)

    conexao.commit()
    conexao.close()
    

def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    print("---LISTAR PROFESSORES---")

    cursor.execute("SELECT * FROM professores") # ESSA É A CHAVE PARA LISTAR
    resultados = cursor.fetchall() # ESSA TAMBÉM

    for professore in resultados:
        print(f"""
              ID: {professore[0]}, 
              NOME: {professore[1]},
              TELEFONE: {professore[2]}, 
              MATERIA: {professore[3]}, 
              IDADE: {professore[4]},
                CPF: {professore[5]},
                SALARIO: {professore[6]},
                ESCOLA: {professore[7]}  
            """)
        print("-" * 30)
    
    conexao.close()

def alterar():
    print("---ALTERAR PROFESSOR---")
    id_prof = int(input("Digite o ID do professor que queira alterar: "))
    novo_nome = input("Digite o nome do professor novo: ")
    novo_telefone = input("Digite o telefone: ")
    novo_materia = input("Digite as matérias do professor: ")
    novo_idade = int(input("Digite a idade do professor: "))
    novo_cpf = input("Digite o CPF do professor: ")
    novo_salario = float(input("Digite o quanto esse professor merece: "))
    novo_escola = input("Digite o nome da escola: ")

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    sql_update = """
    UPDATE professores
    SET nome = ?,
    telefone = ?,
    materia = ?,
    idade = ?,
    cpf = ?,
    salario = ?,
    escola = ?
    WHERE id = ?
    """
    cursor.execute(sql_update, (novo_nome, novo_telefone, novo_materia, novo_idade, novo_cpf, novo_salario, novo_escola, id_prof))

    conexao.commit()
    conexao.close()

def deletar():
    print("---DELETAR PROFESSOR---")
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_prof = int(input("Digite o ID do professor que deseja excluir: "))

    sql_delete = """
    DELETE FROM professores
    WHERE id = ?
    """
    cursor.execute(sql_delete, (id_prof,))

    conexao.commit()
    conexao.close()

def menu():
    opcao = 0

    while opcao != 5:
        print("""   MENU   
                
                1 - CADASTRAR | 
                2 - LISTAR | 
                3 - ALTERAR | 
                4 - EXCLUIR | 
                5 - SAIR
                
                """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            alterar()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            print("Salvando.....")
            print("Salvo")
            print("DESLIGANDO.....")
            break

menu()
