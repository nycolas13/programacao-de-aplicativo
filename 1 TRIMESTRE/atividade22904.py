# Analisador de Desempenho de Equipe
def analisar_vendas(nome,lista_vendas,meta_mensal):
    soma = 0
    for n in lista_vendas:
        soma = soma + n
        media_final = soma / len(lista_vendas)
        
    if media_final >= meta_mensal:
        starus = "bateu"
    else:
        "não bateu"
    return f"O vendedor {nome} teve média de {media_final} e {starus} a meta"

nome_vendedor = "Carlos"
lista = [1200,1500,1100,1900]
meta = 1400
mensagem = analisar_vendas(nome_vendedor,lista,meta)
print(mensagem)