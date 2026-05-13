# Nessa variável é uma variável global, onde ela tem acesso ao código todo.
estoque = []

# Nessa função é a entrada para adicionar um produto.
def adicionar_produto(nome):
    estoque.append(nome)

# Nessa função é uma entrada que acessa uma lista que o ususário vai digitar.
def listar_produtos(produtos):
    for item in produtos:
        indice = produtos.index(item)
        print(f"{indice} - {item}")

# Nessa função é uma entrada que será verificado o indice da lista de estoque que será colocado, usando os caminhos if, elif e else para sabar a posição do indice.
def atualizar_produto(indice, novo_nome,estoque):
    estoque[indice] = novo_nome
 
def remover_produto(indice,estoque):
    if indice < len(estoque):
        estoque.pop(indice)
        print("Produto removido com sucesso!")
    else:
        print("Erro: Não posso remover um item que não existe!")

# Nessa função é um menu interativo onde o def inicia o menu, usando while para repetir os códigos dentro dele até que chega no break que para o loop do while.
def exibir_menu(opcao):
    while opcao != "5":
        print("\n1-adicionar / 2-listar/ 3-atualizar/ 4-remover/ 5-sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            item = input("Nome do produto: ")
            mensagem = adicionar_produto(item)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            produto = input("Digite o nome do produto que quer mudar: ")
            indice = estoque.index(produto)
            novo = input("Digite o novo nome: ")
            mensagem = atualizar_produto(indice, novo, estoque) 
        elif opcao == "4":
            produto = input("Digite o nome do produto que quer remover: ")
            indice = estoque.index(produto)
            mensagem = remover_produto(indice,estoque)
        elif opcao == "5":
            print("Saindo do sistema...")
            return 

# O toque final: Chamar a função com parênteses, que aqui o programa para como se fosse um botão de desligar.
opcao = ""
exibir_menu(opcao)
