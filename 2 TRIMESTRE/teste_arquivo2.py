open("habitos.txt",'w').close()
def cadastrar_habito():
    usuario = input("Insere um novo hábito: ")
    with open("habitos.txt",'a') as lagaptor:
        lagaptor.write(usuario + '\n')

def revisar_mural():
    with open("habitos.txt",'r') as lagaptor:
        habito = lagaptor.readlines()
    p = 0
    for h in habito:
        print(f"{p} - {h.strip()}")
        p += 1 

def editar():
    revisar_mural()
    idx = int(input("O que você quer mudar?: "))
    novo_habito = input("Coloque um novo hábito: ")
    with open("habitos.txt",'r') as lagaptor:
        linhas = lagaptor.readlines()
        linhas[idx] = novo_habito + '\n'
    with open("habitos.txt",'w') as lagaptor:
        lagaptor.writelines(linhas)

def descartar_habito():
    revisar_mural()
    idx = int(input("Escolha de qual hábito deseja remover: "))
    with open("habitos.txt",'r') as lagaptor:
        linhas = lagaptor.readlines()
        del linhas[idx]
    with open('viagens.txt','w') as lagaptor:
        lagaptor.writelines(linhas)

print("---MEUS HÁBITOS---")
opcao = 0
while opcao != 5:
    print("1-Adicionar/ 2-Ver todos/ 3-Editar/ 4-Excluir/ 5-Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_habito()
    elif opcao == "2":
        revisar_mural()
    elif opcao == "3":
        editar()
    elif opcao == "4":
        descartar_habito()
    elif opcao == "5":
        break
print("---ENCERRANDO O PROGRAMA---..........")



