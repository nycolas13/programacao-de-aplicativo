funcionario = input("Você é um ENGENHEIRO ou TÉCNICO?: ")
codigo_de_acesso = int (input("Digite o código: "))
botao = input ("Botão de Emergência pressionado? (S/N): ")
epi = input("Equpamento de proteção completo? (S/N): ")

if (funcionario == "ENGENHEIRO" or funcionario == "TECNICO") and (codigo_de_acesso == 12345 or botao == "S") and epi == "S":
    print("ACESSO LIBERADO")

else:
    print("ACESSO NEGADO")