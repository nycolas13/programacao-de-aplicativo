# O Separador de Números (Lógica e Filtragem)
numeros =[1, 5, 8, 12, 15, 22, 7, 9, 30, 4]
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
        
    elif num % 2 != 0:
        impares.append(num)

print(f"lista pares. {pares}")
print(f"lista impares. {impares}")
