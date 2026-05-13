valor_da_compra = int (input("Digite o valor R$: "))
cliente_prime = input("se você é um cliente prime digite (S/N): ")

frete = 50
valor_total = frete + valor_da_compra

if valor_da_compra > 500 or (cliente_prime == "S" and valor_da_compra < 100):
    print("Você ganha frete grátis")
else:
    print("Você não ganha frete grátis")
