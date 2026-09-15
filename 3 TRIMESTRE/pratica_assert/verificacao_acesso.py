def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False
# Testes com assert
assert pode_entrar(20, False) == True, "Erro: Maior de idade deveria entrar"
assert pode_entrar(15, True)  == True, "Erro: Menor acompanhado deveria entrar"
assert pode_entrar(15, False) == False, "Erro: Menor desacompanhado não deveria entrar"
assert pode_entrar(18, False) == True, "Erro: Pessoa com 18 anos deveria entrar"
assert pode_entrar(17, True)  == True, "Erro: Pessoa com 17 anos acompanhada deveria entrar"

print("Todos os testes passaram com sucesso!")