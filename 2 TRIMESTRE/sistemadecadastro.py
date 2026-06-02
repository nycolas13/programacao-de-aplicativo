import sqlite3

# 1. Interação com o Usuário
print("--- SISTEMA DE CADASTRO DE ALUNOS ---")
nome = input("Nome Completo: ")
telefone = input("Telefone: ")
turma = input("Turma: ")
idade = int(input("Idade: "))  # Garantindo que seja um número inteiro
cpf = input("CPF: ")

# 2. Conexão com o Banco de Dados
conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

# Coloque isso logo após o: cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    turma TEXT,
    idade INTEGER,
    cpf TEXT
)
""")

# 3. Comando SQL usando F-String (Atenção às aspas para TEXT e sem aspas para INTEGER)
comando_sql = f"INSERT INTO alunos (nome, telefone, turma, idade, cpf) VALUES ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}')"

# 4. Execução e Gravação
cursor.execute(comando_sql)
conexao.commit()

# 5. Fechando a conexão e Feedback
conexao.close()
print("\n[Sucesso] Aluno cadastrado com sucesso!")