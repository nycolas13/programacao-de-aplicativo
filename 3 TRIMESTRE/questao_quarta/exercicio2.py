def buscar_sequencial(vetor, alvo):
    contador = 0
    for e in vetor:
        if e == alvo:
            contador += 1
    return contador

numeros = [2, 3, 4, 5, 7, 8, 5, 6, 5]
alvo = 5
print(f"O número {alvo} aparece {buscar_sequencial(numeros, alvo)} vezes.")
