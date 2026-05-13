livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
nome_livro = input("Digite o nome do livro: ")

# Operação de Empréstimo
if nome_livro in livros_disponiveis:
    livros_disponiveis.remove(nome_livro)
    livros_emprestados.append(nome_livro)
else:
    print("Desculpe, este livro não está no acervo.")

# Operação de Devolução
nome_livro2 = input("digita o nome do livro que está devolvendo: ")
if nome_livro2 in livros_emprestados:
    livros_emprestados.remove(nome_livro2)
    livros_disponiveis.append(nome_livro2)
else:
    print( "Este livro não consta como emprestado.")

# Manutenção do Acervo
del livros_disponiveis[0:2]

# Relatório Final
print(f"Estado final das duas listas. {livros_disponiveis} e {livros_emprestados}.")