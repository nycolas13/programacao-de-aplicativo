import json
import os

ARQUIVO_JSON = "alunos.json"

# Funções Auxiliares para o Arquivo
def carregar_dados():
    if not os.path.exists(ARQUIVO_JSON):
        return []
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_dados(alunos):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)

# 1. CADASTRAR ALUNO (C)
def cadastrar_aluno():
    print("\n--- CADASTRAR NOVO ALUNO ---")
    alunos = carregar_dados()
    id_digitado = int(input("Digite o ID do aluno: "))

    # Validação de ID único
    id_existe = any(aluno['id'] == id_digitado for aluno in alunos)

    if id_existe:
        print("Erro crítico: Esse número de ID já foi usado por outro aluno!")
        return

    novo_aluno = {
        "id": id_digitado,
        "nome": input("Nome Completo: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    }
    
    alunos.append(novo_aluno)
    salvar_dados(alunos)
    print("[Sucesso] Aluno cadastrado com sucesso!")

# 2. LISTAR ALUNOS (R)
def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")
    alunos = carregar_dados()
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
        
    for aluno in alunos:
        print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | Turma: {aluno['turma']} | Idade: {aluno['idade']} | Tel: {aluno['telefone']} | CPF: {aluno['cpf']}")

# 3. ATUALIZAR DADOS (U)
def atualizar_aluno():
    print("\n--- ATUALIZAR ALUNO ---")
    alunos = carregar_dados()
    id_busca = int(input("Digite o ID do aluno que deseja alterar: "))
    
    for aluno in alunos:
        if aluno['id'] == id_busca:
            print(f"Editando dados de: {aluno['nome']}\n(Pressione Enter para manter o valor atual)")
            
            nome = input(f"Novo Nome [{aluno['nome']}]: ")
            telefone = input(f"Novo Telefone [{aluno['telefone']}]: ")
            turma = input(f"Nova Turma [{aluno['turma']}]: ")
            idade_txt = input(f"Nova Idade [{aluno['idade']}]: ")
            cpf = input(f"Novo CPF [{aluno['cpf']}]: ")
            
            # Atualiza apenas se o usuário digitou algo
            if nome: aluno['nome'] = nome
            if json: aluno['telefone'] = telefone
            if turma: aluno['turma'] = turma
            if idade_txt: aluno['idade'] = int(idade_txt)
            if cpf: aluno['cpf'] = cpf
            
            salvar_dados(alunos)
            print("[Sucesso] Dados atualizados!")
            return
            
    print("Erro: Aluno não encontrado.")

# 4. REMOVER ALUNO (D)
def remover_aluno():
    print("\n--- REMOVER ALUNO ---")
    alunos = carregar_dados()
    id_busca = int(input("Digite o ID do aluno que deseja excluir: "))
    
    for aluno in alunos:
        if aluno['id'] == id_busca:
            alunos.remove(aluno)
            salvar_dados(alunos)
            print("[Sucesso] Aluno removido do sistema!")
            return
            
    print("Erro: Aluno não encontrado.")

# Menu Principal Interativo
def menu():
    while True:
        print("\n=== SISTEMA DE MATRÍCULA ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1": cadastrar_aluno()
        elif opcao == "2": listar_alunos()
        elif opcao == "3": atualizar_aluno()
        elif opcao == "4": remover_aluno()
        elif opcao == "5": 
            print("Encerrando o sistema...")
            break
        else: 
            print("Opção inválida!")

if __name__ == "__main__":
    menu()