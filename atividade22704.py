# Calculadora de Área de Terrenos (Geometria)
def calcular_area(*largura,comprimento):
    calculo = 0
    for n in largura:
        calculo * n
        return calculo
    for n in comprimento:
        calculo * n
        return calculo

lista_terrenos_largura = [10,5,12,2,15,0]
lista_terrenos_comprimento = [20,5,30,6,50,3]
mensagem = calcular_area(lista_terrenos_largura, lista_terrenos_comprimento)
print(f"área 1 {lista_terrenos_largura} área 2 {lista_terrenos_largura} área 3 {lista_terrenos_largura}. comprimento 1 {lista_terrenos_comprimento}, comprimento 2 {lista_terrenos_comprimento} comprimento 3 {lista_terrenos_comprimento}")