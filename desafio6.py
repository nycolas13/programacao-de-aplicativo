# Configuração inicial
lista_autorizados = ["Alice","Bob","Carlos"]
nome = input("Digite o nome de um pesquisador: ")

# Verifição de Existencia
if nome == lista_autorizados:
    lista_autorizados.index(2)
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {lista_autorizados}.")
usuario = input("Você deseja remover esse pesquisador da lista (S/N): ")
if usuario == "S":
    lista_autorizados.remove(2)
    print(f"lista atualizada {lista_autorizados}")
elif lista_autorizados:
    print(f"Acesso Negado! O pesquisador {nome} não foi encontrado.")
usuario = input("Deseja cadastrar esse novo pesquisador (S/N): ")
if usuario == "S":
    lista_autorizados.apped()
    