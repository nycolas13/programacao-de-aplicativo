def somar_carrinho (lista_precos_produtos):
    soma = 0
    for n in lista_precos_produtos:
        soma += n
    if soma > 500.00:
        desconto = soma * 0.10
        total = soma - desconto
        return total
    else:
        return soma
lista_compras = [12.00,15.00,10.00,100.00]
mensagem_conta = somar_carrinho(lista_compras)
print(f"Valores que o cliente deve pagar: {mensagem_conta}")