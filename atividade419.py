vagas = ["Livre","Ocupado","Livre","Ocupado"]
usuario = int(input("Digite o número de uma vaga de 0 a 3: "))

if usuario % 2 == 0 and vagas[usuario] == "Livre":
    print("autorizada para estacionar.")
else:
    print(f"Vaga {usuario} indisponível ou fora das regras.")