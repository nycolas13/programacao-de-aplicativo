cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
nome_cidade = input("Digite um nome de uma cidade: ")

if nome_cidade in cidades:
    indice = cidades.index(nome_cidade)
    print(f"A cidade {nome_cidade} está na posição {indice}.")
else:
    print("Cidade não encontrada!")