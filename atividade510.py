codigo_pacote = int(input("Digite o código dos pacotes: "))
peso = int(input("Digite o peso dos pacotes: kg "))

if peso < 5 and (codigo_pacote % 10):
    print("Pacote {codigo}: [ENTREGA EXPRESSA]") 
elif peso > 50:   
    print("Pacote {codigo}: [CARGA PESADA]")