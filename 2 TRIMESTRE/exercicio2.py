import json

# Esse mini-script cria o arquivo exatamente onde o Python está rodando
dados_iniciais = {"matematica": 8.5, "portugues": 9.0}

with open("notas.json", "w") as arquivo:
    json.dump(dados_iniciais, arquivo)

print("Arquivo criado com sucesso no lugar certo! Agora você pode rodar o script de leitura")

# Recupera as notas do dicionário
nota_matematica = dados_iniciais["matematica"]
nota_portugues = dados_iniciais["portugues"]

# Calcula a soma
soma = nota_matematica + nota_portugues

# Mostra o resultado na tela
print(f"Nota de Matemática: {nota_matematica}")
print(f"Nota de Português: {nota_portugues}")
print(f"A soma das duas notas é: {soma}")