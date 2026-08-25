def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20
# Testes para calcular_frete
assert calcular_frete(50) == 20, "Erro: Compra abaixo de 100 deve pagar 20"
assert calcular_frete(100) == 10, "Erro: Compra de exatamente 100 deve pagar 10"
assert calcular_frete(150) == 10, "Erro: Compra entre 100 e 199.99 deve pagar 10"
assert calcular_frete(200) == 0, "Erro: Compra de exatamente 200 deve ter frete grátis (0)"
assert calcular_frete(250) == 0, "Erro: Compra acima de 200 deve ter frete grátis (0)"

print("Todos os testes de frete passaram com sucesso!")