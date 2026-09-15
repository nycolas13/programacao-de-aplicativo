def acha_maior(vetor):
    if not vetor:
        return None, None
        
    maior = vetor[0]
    indice = 0
    
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            indice = i
            
    return maior, indice

# Exemplo:
numeros = [14, 25, 3, 42, 59, 61, 78, 8, 90, 10]
maior_valor, posicao = acha_maior(numeros)

print(f"Maior número: {maior_valor} (na posição {posicao})")     