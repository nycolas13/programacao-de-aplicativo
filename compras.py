valor = float (input("Digite o valor total: "))
cupom = (input("Digite o nome do cupom: "))

desconto = valor * 0.10
novo_preco = valor - desconto

if cupom == "DEV10":
    print("cupom valido", novo_preco)
else:
    print("cupom invalido", valor)


