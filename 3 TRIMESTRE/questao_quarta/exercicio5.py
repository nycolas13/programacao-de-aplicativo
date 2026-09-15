def busca_primeira_ultima(vetor, alvo):
    primeiro = -1
    ultimo = -1
    for i in range(len(vetor)):
        if vetor[i] == alvo:
            if primeiro == -1:
                primeiro = i
            ultimo = i
    return primeiro, ultimo

# Exemplo:
numeros = [5, 2, 5, 7, 5, 9]
alvo = 5
print(busca_primeira_ultima(numeros, alvo)) # Saída: (0, 4)