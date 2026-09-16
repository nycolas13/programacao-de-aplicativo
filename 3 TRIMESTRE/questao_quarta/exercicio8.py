def busca_binaria_contada(vetor, alvo):
    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0
    
    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        
        if vetor[meio] == alvo:
            return meio, comparacoes
        elif vetor[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return -1, comparacoes

# Exemplo:
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
alvo = 70
indice, total = busca_binaria_contada(numeros, alvo)
print(f"Índice: {indice} | Comparações: {total}")