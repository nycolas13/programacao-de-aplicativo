import json

caixas = {
            "nome": input("nome: "),
            "idade": int(input("idade: ")),
            "cpf": int(input("cpf: "))
        }

with open("aprendiz.json",'w',encoding='utf-8') as arquivo:
    json.dump(caixas,arquivo,indent=4)
    
with open("aprendiz.json",'r',encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
for itens in dados.items():
    print("\nDados lidos no arquivo:")
    print(dados)
    
    




