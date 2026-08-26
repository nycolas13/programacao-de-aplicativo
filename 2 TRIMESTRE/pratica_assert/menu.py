import fabricante
import posto


def menu ():
    opcao = "0" 
    while opcao != "9":
        print("=== Sistema de Gerenciamento ===")
        print("1. Cadastrar Fabricante")
        print("2. Listar Fabricante")
        print("3. Atualizar Fabricante")
        print("4. Excluir Fabricante")
        print("5. Cadastrar Posto")
        print("6. Listar Posto")
        print("7. Atualizar Posto")
        print("8. Excluir Posto")
        print("9. Sair")

        opcao = input("Escolher uma opção: ")

        if opcao == "1":
            fabricante.cadastrar_fabricante()
        elif opcao == "2":
            fabricante.listar_fabricante()
        elif opcao == "3":
            fabricante.atualizar_fabricante()
        elif opcao == "4":
            fabricante.excluir_fabricante()
        elif opcao == "5":
            posto.cadastrar_posto()
        elif opcao == "6":
            posto.listar_posto()
        elif opcao == "7":
            posto.atualizar_posto()
        elif opcao == "8":
            posto.excluir_posto()


menu()