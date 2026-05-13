peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

if imc > 25:
    print(f"IMC: {imc:.2f} - Sobrepeso")
else:
    print(f"IMC: {imc:.2f} - Peso normal ou abaixo")