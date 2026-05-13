nome_de_usuario = input("Digite seu nome: ")
senha = int (input("Digite a senha: "))

if (nome_de_usuario == "Adim" or nome_de_usuario == "root") and senha == 12345:
    print("Acesso liberado")
else:
    print("Acesso negado")