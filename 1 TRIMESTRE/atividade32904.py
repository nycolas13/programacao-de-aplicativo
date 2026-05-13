def gerar_relatorio(nome, peso, altura, idade):
    imc = peso/(altura ** 2)
    if imc < 18.5:
        categoria = "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        categoria = "Normal"
    elif 25 <= imc <= 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    relatorio = f"Olá {nome}! com {idade} anos, seu IMC é {imc:.2f} e sua categoria é: {categoria}."
    return relatorio
print("----SISTEMA DE SAÚDE----")
nome_usuario = input("Digite seu nome: ")
peso_usuario = float(input("Digite seu peso (kg): "))
altura_usuario = float(input("Digite sua altura (ex: 1.75): "))
idade_usuario = int(input("Digite sua idade: "))
resultado_final = gerar_relatorio (nome_usuario, peso_usuario, altura_usuario, idade_usuario)
print("\n" + resultado_final)