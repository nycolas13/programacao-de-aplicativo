def posicao_insercao(vetor, alvo):
    inicio, fim = 0, len(vetor)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if vetor[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio
    return inicio

# Exemplo:
numeros = [10, 20, 40, 50]
print(posicao_insercao(numeros, 30))  # Retorna o índice 2