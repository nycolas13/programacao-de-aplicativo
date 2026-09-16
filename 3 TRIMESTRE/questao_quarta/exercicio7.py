def busca_binaria_palavra(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False

# Exemplo:
palavras = ["abacaxi", "bola", "casa", "dado", "elefante"]
alvo = "casa"

print(busca_binaria_palavra(palavras, alvo)) # Retorna True