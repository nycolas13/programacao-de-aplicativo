#Parte 1
saldo_inicial = 1000.00
menu_de_opcoes = input("Escolhe 1(depósito); 2(saque) ou 3(extrato): ")

#Parte 2
if menu_de_opcoes == "1":
    valor = float (input("Dinheiro"))
    if valor > 0:
        saldo_inicial = saldo_inicial + valor
        print(" Novo saldo: ", saldo_inicial)

elif menu_de_opcoes == "2":
