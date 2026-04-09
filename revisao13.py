# Sistema de login (3 tentativas)
senha_correta = "1234"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso concedido!")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Você tem {tentativas} tentativas.")

if tentativas == 0:
    print("Acesso negado.")