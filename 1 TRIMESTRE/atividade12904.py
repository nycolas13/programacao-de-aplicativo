# Sistema de Checkout com Imposto e Desconto
def calcular_preco_final(valor_base,imposto_percentual,cupom_desconto):
    valor = valor_base - imposto_percentual
    preco_final =  valor - cupom_desconto

    if cupom_desconto > valor_base:
        return 0
        return preco_final

usuario1 = int(input("Digite um valor: "))
usuario2 = int(input("digite o imposto: "))
usuario3 = int(input("Digite o cupom: "))
mensagem = calcular_preco_final(usuario1,usuario2,usuario3)
print(f"Preço final: {mensagem}")