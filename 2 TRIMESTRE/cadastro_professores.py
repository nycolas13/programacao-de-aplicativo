import sqlite3 

def cadastrar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = cursor.conexao

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
    cursor = cursor.conexao

    cursor.execute("SELECT * FROM professores") # ESSA É A CHAVE PARA LISTAR
    resultados = cursor.fetchall() # ESSA TAMBÉM

    for professore in resultados:
        print(f"ID: {professore[0]}, NOME: {professore[1]},TELEFONE: {professore[2]}")