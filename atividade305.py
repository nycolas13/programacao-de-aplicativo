temperetura = float(input("Qual a temperatura atual? C: "))

if temperetura <= 30:
    print("Clima estável")
elif temperetura > 30:
    print("Alerta de calor!")
    umidade = float(input("Peça umidade: "))
    if umidade < 40.0:
        print("Ação: Ligar irrigação!")
    else:
        print("Ação: Ligar apenas ventiladores")