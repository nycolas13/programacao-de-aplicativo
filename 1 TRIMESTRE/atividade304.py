# Aplicador de Descontos (Listas + Funções)
def aplicar_promocao (lista_precos, lista_desconto):
    for n in lista_precos:
        if n >= 100.0:
            desconto = n * 0.15
            novo_valor = n - desconto
            lista_desconto.append(novo_valor)
    return lista_desconto   
        

lista_compras = [150.0, 80.0, 200.0, 50.0]
lista_compras_nova = []
desconto_recebido = aplicar_promocao(lista_compras, lista_compras_nova)
print(f" O resultado da nova lista{desconto_recebido}")
