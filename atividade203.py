media_do_aluno = float (input("Qual a sua média?: "))
renda = float (input("Qual sua renda?: "))
escola_publica = input("Você veio em escola pública? (S/N): ")

if media_do_aluno > 8.0 and (renda < 2000.00 or escola_publica == "S"):
    print("Ganhou a bolsa")
else:   
    print("Não atende os requisitos")