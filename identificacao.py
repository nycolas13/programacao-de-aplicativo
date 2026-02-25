nome = (input("Digite seu nome: "))
altura = int(input("Digite sua altura: "))

if altura < 150.00:
    print("desculpe, você não tem altura minima", nome)
elif altura >= 150.00:
    print("Acesso liberado! Divirta-se na queda livre", nome)

