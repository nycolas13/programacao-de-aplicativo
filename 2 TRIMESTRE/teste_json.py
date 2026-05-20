import json


open("matricula.json", 'w').close()
identidade = int(input("Digite seu CPF: "))
nome = input("Digite seu nome: ")
numero = int(input("Digite seu número: "))
classe = input("Digite sua turma: ")
idade = int(input("Digite sua idade: "))
aluno = {"cpf": identidade, 
        "nome completo": nome,
        "telefone": numero,
        "turma": classe,
        "idade": idade
        }
def cadastrar_aluno():
    with open("matricula.json",'a') as matricula_json:
        json.dump(aluno, matricula_json,ident=4, ensure_ascii=false)

    if aluno["cpf"] 
    
    
