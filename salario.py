salario = float (input ("digite o seu salário: "))

if salario >= 10000.00:
    print("Rico")
elif salario >= 5000.00:
    print("Classe média")
elif salario < 5000.00:
    print("Classe baixa")