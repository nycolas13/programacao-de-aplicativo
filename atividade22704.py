# Calculadora de Área de Terrenos (Geometria)
def calcular_area(*largura,*comprimento):
    for n in largura:
        if n == 3:
            multiplicacao1 = n * largura
            multiplicacao2 = multiplicacao1 * comprimento
    return multiplicacao2

lista_terrenos_largura = [10,5,12,2,15,0]
lista_terrenos_comprimento = [20,5,30,6,50,3]
Terrenos1 = int(input("Digite da área 1: "))
Terrenos2 = int(input("Digite da área 2: "))
Terrenos3 = int(input("Digite da área 3: "))
mensagem = calcular_area(Terrenos)