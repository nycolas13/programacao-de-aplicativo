saldo = 1000.0

print("--- CAIXA ELETRÔNICO ---")
print("1 - Depósito")
print("2 - Saque")
print("3 - Extrato")

opcao = input("Escolha a operação: ")

# 3. EXTRATO
if opcao == "3":
    print(f"SEU SALDO ATUAL: R$ {saldo}")

# 1. DEPÓSITO
elif opcao == "1":
    valor = float(input("Quanto deseja depositar? R$ "))
    if valor > 0:
        saldo += valor
        print(f"Depósito de R$ {valor} realizado!")
        print(f"Novo saldo: R$ {saldo}")
    else:
        print("Operação cancelada: Valor de depósito inválido.")

# 2. SAQUE
elif opcao == "2":
    valor = float(input("Quanto deseja sacar? R$ "))
    
    if valor > 0 and (valor <= saldo or valor == 100.0):
        saldo -= valor
        print(f"Saque de R$ {valor} realizado!")
        print(f"Saldo restante: R$ {saldo}")
    else:
        print("Operação negada: Saldo insuficiente ou valor inválido.")

else:
    print("Opção inválida!")
