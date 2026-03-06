comprimento_peca = input("O comprimento da peça está 10cm e 12cm? (S/N): ")

if comprimento_peca == "S": 
    largura = input("A largura está entre 5cm e 6cm? (S/N): ")
    if largura =="S" :
        print("Peça aprovada")
    else:
        print("REPROVADO: Problema na largura")
else:
    print("REPROVADO: Problema no comprimento")
