estoque = []

def adicionar_produto(nome):
    estoque.append(nome)


def listar_produtos():
    for i, produtos in enumerate(estoque):
        print(f"{i} - {produtos}")


def atualizar_produto(indice, novo_nome):
    estoque[indice] = novo_nome
    if indice < len(estoque):
        estoque[indice] = novo_nome
        print("Produto atualizado com sucesso!")
    else:
        print("Erro: Este índice não existe no estoque!")

    if indice < len(estoque):
        estoque.pop(indice)
        print("Produto removido com sucesso!")
    else:
        print("Erro: Não posso remover um item que não existe!")

def exibir_menu():
    while True:
        print("\n1-adicionar / 2-listar/ 3-atualizar/ 4-remover/ 5-sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            item = input("Nome do produto: ")
            adicionar_produto(item)
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            idx = int(input("Digite o número (índice) do produto que quer mudar: "))
            novo = input("Digite o novo nome: ")
            atualizar_produto(idx, novo) # Passando os dados para a função
        elif opcao == "4":
            idx = int(input("Digite o número (índice) do produto que quer remover: "))
            remover_produto(idx)
        elif opcao == "5":
            print("Saindo do sistema...")
            break

# O toque final: Chamar a função com parênteses
exibir_menu()