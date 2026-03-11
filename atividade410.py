senha = int(input("Digite a senha: "))
tentativa_atual = int(input("Digite números: "))
token = input("Possui o Token? (S/N): ")

if (senha == 123) and (tentativa_atual % 3 == 0 or token == "S"):
    print("ACESSO CONCEDIDO")
else:
    print("ACESSO BLOQUEADO por PROTOCOLO")