comprimento_peca = input("O comprimento da peça está 10cm e 12cm? (S/N): ")

if comprimento_peca == "N":
    print("REPROVADO: Problema no comprimento")
elif comprimento_peca == "S":
    print("A largura está entre 5cm e 6cm? (S/N): ")
    if comprimento_peca == "S":
        print("Peça aprovada")
    else:
        print("REPROVADO: Problema na largura")