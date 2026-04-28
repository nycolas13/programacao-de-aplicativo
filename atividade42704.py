def somar_carrinho (lista_precos_produtos):
    somar = 0
    soma = somar + lista_precos_produtos
    if soma > 500.00:
        desconto = soma * 0.10
        return desconto
    else:
        return soma