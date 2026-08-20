def eh_par(numero):
    return numero % 2 == 0

def executar_testes():
    # 1. Número par positivo
    assert eh_par(4) is True, " 4 deve ser par"

    # 2. Número ímpar positivo
    assert eh_par(7) is False, " 7 deve ser ímpar"

    # 3. Zero
    assert eh_par(0) is True, " 0 deve ser par"

    # 4. Número negativo
    assert eh_par(-2) is True, "-2 deve ser par"
    assert eh_par(-3) is False, " -3 deve ser ímpar"

    print("Todos os testes passaram com sucesso!")

executar_testes()