import json

# Solicita a frase ao usuário
frase_usuario = input("Digite uma frase: ")

# Cria o dicionário com a chave "mensagem"
dados = {
    "mensagem": frase_usuario
}

# Salva o dicionário no arquivo teste.json
with open("teste.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("Arquivo 'teste.json' criado com sucesso!")