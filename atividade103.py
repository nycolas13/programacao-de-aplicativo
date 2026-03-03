cliente = int (input("quantos anos tem?: "))
ingreso_vip = input("possui o inresso? (S/N): ")
lista = input("está na lista? (S/N): ")

if cliente > 18 and (ingreso_vip == "S" or lista == "S"):
    print("Seja bem-vindo!")
elif cliente < 18 and (ingreso_vip == "S" or lista == "S"):
    print("Recusado")