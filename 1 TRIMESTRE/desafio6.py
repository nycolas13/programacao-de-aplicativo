# Configuração inicial
lista_autorizados = ["Alice","Bob","Carlos"]
nome = input("Digite o nome de um pesquisador: ")

# Verifição de Existencia
if nome in lista_autorizados:
    indice = lista_autorizados.index(nome)
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}.")

    remover = input("Você deseja remover esse pesquisador da lista (S/N): ")
    if remover == "S":
        lista_autorizados.remove(nome)
        print(f"lista atualizada {lista_autorizados}")
else:
    print(f"Acesso Negado! O pesquisador {nome} não foi encontrado.")
    adicionar = input("Deseja cadastrar esse novo pesquisador (S/N): ")
    if adicionar == "S":
        lista_autorizados.append(nome)
        print(f"lista atual{lista_autorizados}")