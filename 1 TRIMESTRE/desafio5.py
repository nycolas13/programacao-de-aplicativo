# parte1
garrafas = int (input("Digite o número de garrafas: "))


if garrafas == 500 :
    print("HORA DA LIMPEZA:Parar máquina imediatamente!")
    print("QUALIDADE:Retirar amostra para teste")

elif garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")

elif garrafas % 100 == 0:
    print("QUALIDADE:Retirar amostra para teste")
     
else:
    print("Produção em dia.")