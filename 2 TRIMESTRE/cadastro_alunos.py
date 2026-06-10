import sqlite3

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
telefone_aluno = input("Telf(): ")
turma_aluno = input("Classificação de turma: ")
idade_aluno = int(input("Idade do Aluno: "))
cpf_aluno = input("CPF do aluno: ")

comando_inserir = f'''
                    INSERT INTO alunos(
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
print("--DESLIGANDO......")
print(".")


conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS aluno(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL
                )''')

cursor.execute("SELECT * FROM alunos")
resultados = cursor.fetchall()

print("--- DADOS DOS ALUNOS CADASTRADOS ---")
for aluno in resultados:
    print(f"ID: {aluno} | Nome: {aluno} | Tel: {aluno} | Turma: {aluno} | Idade: {aluno} | CPF: {aluno}")

# 5. Fecha a conexão
conexao.close()
print("--DESLIGANDO......")
