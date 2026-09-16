def busca_binaria(vetor, alvo):
    inicio = 0
    fim = len(vetor) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if vetor[meio] == alvo:
            return meio  # Encontrou
        elif vetor[meio] < alvo:
            inicio = meio + 1  # Busca na metade da direita
        else:
            fim = meio - 1  # Busca na metade da esquerda
            
    return -1  # Não existe no vetor

# Exemplo (precisa estar ordenado!):
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
alvo = 50

print(f"Índice encontrado: {busca_binaria(numeros, alvo)}")