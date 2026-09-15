def busca_sequencial(vetor, alvo):
    for i in range(len(vetor)):
        if vetor[i] == alvo:
            return i
    return -1  # Retorna -1 se o número não estiver no vetor

# Exemplo de uso:
numeros = [14, 25, 3, 42, 59, 61, 78, 8, 90, 10]
alvo = 59

indice = busca_sequencial(numeros, alvo)
print(f"Índice encontrado: {indice}")