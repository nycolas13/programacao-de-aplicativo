def seq_comp(v, alvo):
    for i, val in enumerate(v):
        if val == alvo:
            return i + 1
    return len(v)

def bin_comp(v, alvo):
    inicio, fim, comp = 0, len(v) - 1, 0
    while inicio <= fim:
        comp += 1
        meio = (inicio + fim) // 2
        if v[meio] == alvo:
            return comp
        elif v[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return comp

vetor = list(range(1, 101))
alvos = [15, 50, 85]

for a in alvos:
    print(f"Alvo {a}: Sequencial = {seq_comp(vetor, a)} | Binária = {bin_comp(vetor, a)}")