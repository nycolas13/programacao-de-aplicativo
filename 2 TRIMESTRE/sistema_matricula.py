import json
import os

arquivo = "alunos.json"

def criar():
    if os.path.exists(arquivo):
        with open(arquivo,'r', encoding="utf-8") as ID:
            alunos = json.load(ID)
    else:
        alunos = []
    
    
    novo_aluno = {
        "id": int(input("Digite seu ID: ")),
        "nome": input("Digite o nome completo: "),
        "telefone": input("Digite seu telefone: "),
        "turma": input("Qual é a sua turma: "),
        "idade": int(input("Digite sua idade: ")),
        "cpf": int(input("Digite seu CPF: ")),
        }

    for aluno in alunos:
        if aluno["id"] == novo_aluno["id"]:
            print("Erro: Este ID já está em uso!")
            return
        else:
            novo_aluno = {
        "id": int(input("Digite seu ID: ")),
        "nome": input("Digite o nome completo: "),
        "telefone": input("Digite seu telefone: "),
        "turma": input("Qual é a sua turma: "),
        "idade": int(input("Digite sua idade: ")),
        "cpf": int(input("Digite seu CPF: ")),
        }
criar()
   


def listar():
    if os.path.exists(arquivo):
        with open(arquivo,'r', encoding="utf-8") as ID:
            alunos = json.load(ID)
    else:
        alunos = []
    