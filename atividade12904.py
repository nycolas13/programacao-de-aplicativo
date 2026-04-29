# Sistema de Checkout com Imposto e Desconto
def calcular_preco_final(valor_base,imposto_percentual,cupom_desconto)
    valor = imposto_percentual + valor_base
    subtrair = cupom_desconto - valor
    if cupom_desconto > valor:
        