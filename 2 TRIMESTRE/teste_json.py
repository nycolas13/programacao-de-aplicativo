import json

def criar_arquivo():
    open("matricula.json", 'w').close()

def cadastrar_aluno():
    nome = input("Digite seu nome: ")
    numero = int(input("Digite seu número: "))
    classe = input("Digite sua turma: ")
    idade = int(input("Digite sua idade: "))
    aluno = {"nome completo": nome,
            "telefone": numero,
            "turma": classe,
            "idade": idade
            }
    with open("matricula.json",'a') as matricula_json:
        json.dump(aluno, matricula_json,ident=4, ensure_ascii=false)

def listar_aluno():
    with open("matricula.json",'r') as matricula_json:
        dados_cadastrados = json.loard(matricula_json)
    print(f"O aluno {aluno["nome completo"]} - {aluno["telefone"]} - {aluno["turma"]} - {aluno["idade"]} foi matriculado {dados_cadastrados}")

def atualizar_dados():
    listar_aluno()
    idx = input("Digite o nome que quer alterar: ")
    nome_novo = input("Digite o novo nome: ")
    idx = int(input("Dgite o telefone que quer mudar: "))
    novo_telefone = int(input("Digite o novo telefone: "))
    idx = input("Digite a classe que quer mudar: ")
    nova_classe = input("Digite a nova classe: ")
    idx = int(input("Digite a idade que quer mudar: "))
    nova_idade = int(input("Digite a nova idade: "))    
    with open("matricula.json",'w') as matricula_json:
        json.dump(aluno, matricula_json,ident=4, ensure_ascii=false)
    print("Dados atualizados")

def remover_aluno():
    listar_aluno()
    idx = int("Digite o nome que quer excluir: ")