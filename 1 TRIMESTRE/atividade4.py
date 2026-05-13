temperatura_atual = float (input("qual a temperatura atual?: "))

if temperatura_atual >= 80:
    print("PERIGO! Desliguando servidor por superaquecimento!")
if temperatura_atual >= 50:
    print("ALERTA: Ventoinhas ligadas ao máximo")