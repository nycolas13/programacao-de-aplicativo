media = float (input("peça a média: "))
presenca = int (input("porcentagem de presença 0 a 100: "))

if media >= 7.0 and presenca >= 75:
    print("Parábens! você foi aprovado")
elif media < 7.0 and presenca < 75:
    print("Reprovado")