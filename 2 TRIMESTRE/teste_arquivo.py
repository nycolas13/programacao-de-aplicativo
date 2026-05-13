open('viagens.txt','w').close()
def criar():
    nome = input("Opção de cidade: ")
    with open('viagens.txt','a') as destino:
        destino.write(nome + '\n')

def ler():
    with open('viagens.txt','r') as destino:
        viagens = destino.readlines()

    p = 0
    for v in viagens:
       print(f"{p} - {v.strip()}") 
       p += 1                                                                
def atualizar():
    ler()
    idx = int(input("Digite a escolha que quer trocar: "))
    novo_nome = input("Digite o outro nome: ")
    with open('viagens.txt','r') as destino:
        linhas = destino.readlines()
        linhas[idx] = novo_nome + '\n'
    with open('viagens.txt','w') as destino:
        destino.writelines(linhas)
def remover():
    ler()
    idx = int(input("Digite o nome que quer excluir: "))
    with open('viagens.txt','r') as destino:
        linhas = destino.readlines()
    del linhas[idx]
    with open('viagens.txt','w') as destino:
        destino.writelines(linhas)



opcao = 0
while opcao != 5:
    print("1-Adicionar Destino/ 2-Listar Sugestões/ 3-Editar Sugestões/ 4-Remover Sugestões/ 5-Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        criar()
    elif opcao == "2":
        ler()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        remover()
    elif opcao =="5":
        break

print ("----PLANEJADOR DE VIAGENS----")