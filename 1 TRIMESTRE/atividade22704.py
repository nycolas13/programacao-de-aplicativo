def calcular_area(largura,comprimento): 
    rodar = 0
    while rodar <= 3:
        rodar += 1
        multiplicar = largura * comprimento
        return multiplicar
usuario_largura = int(input("Digite o valor da largura: "))
usuario_compriemto = int(input("Digite o volar do comprimento:"))
mensagem = calcular_area(usuario_largura,usuario_compriemto)
print(f"Valor da área do terreno 1 é: {mensagem}")
print(f"Valor da área do terreno 2 é: {mensagem}")
print(f"Valor da área do terreno 3 é: {mensagem}")