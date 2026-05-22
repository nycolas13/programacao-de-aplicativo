# O import json serve para importar e buscar ferramentas para seu uso(json.load, json.dump)
import json
# O import os importa acesso aos (os.path.exists() para ver se o arquivo existe)
import os

# Criando o arquivo
BANCO_DADOS = 'alunos.json'

# Criando o cadastro do aluno
def cadastrar():
    print("\n--- Novo Cadastro ---")
    
    # Se o arquivo existe que no caso é o "BANCO_DADOS"
    if os.path.exists(BANCO_DADOS):

        # Abrindo o arquivo
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            alunos = json.load(f) # Lendo o arquivo (f) nome substitudo do (BANCO_DADOS)

    # Se caso o meu arquivo não existir, ele vai criar um novo arquivo que vai ser uma lista guardando todo o objeto da variável aluno nessa lista
    else:
        alunos = []

    # Objetos do sujeito
    novo_aluno = {
        "nome": input("Nome: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    }
    
    alunos.append(novo_aluno) # Adicionando os objetos do (novo_aluno) para a lista (alunos)

    # Abrindo o arquivo e sobrescrevendo o que digitar cada objeto do (novo_aluno)
    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
        
    print("Aluno cadastrado com sucesso!")

def listar(): # Criando uma função
    print("\n--- Lista de Alunos ---")
    
    if os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # Abrindo o arquivo para ler o que foi salvo em (novo_aluno)
            alunos = json.load(f)
    else:
        alunos = [] # Se caso o arquivo não existir ainda, ele vai mostrar a lista vazia, como forma de segurança

    if not alunos: # Se não encontrar nenhuma informação 
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos: # Verificando se está tudo na lista e exibi-la 
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

def atualizar(): # Criando uma função
    print("\n--- Atualizar Aluno ---")
    if not os.path.exists(BANCO_DADOS): # Se o arquivo não existi, exibi "Nenhum aluno cadastrado no sistema"
        print("Nenhum aluno cadastrado no sistema.")
        return 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ") # Editando o cpf
    
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca: # Se o objeto ("cpf") for igual da variavel (cpf_busca) vai ocorrer a seguinte ação
            print(f"Editando dados de: {aluno['nome']}") 
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # Exibe o nome que foi salvo e ao mesmo tempo ele pede para digitar um novo nome
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            # Abrindo o arquivo para sobrescrever as novas atualizações
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()