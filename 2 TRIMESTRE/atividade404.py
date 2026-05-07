#O Localizador de Itens (Busca em Lista)
def esta_na_lista(lista_nomes, nome_busca):
    for n in lista_nomes:
        if nome_busca == n:
            return "ENCONTRADO"
    if n != nome_busca:
        return "Não disponivel"

lista_frutas = ["maça","banana","goiaba", "laranja"]
busca_frutas = input("digite a fruta: ")
mensagem = esta_na_lista(lista_frutas, busca_frutas)
print(mensagem)