def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)
# Produto sem desconto (0%)
assert calcular_desconto(100, 0) == 100

# Produto com 10% de desconto
assert calcular_desconto(100, 10) == 90

# Produto com 50% de desconto
assert calcular_desconto(100, 50) == 50

# Produto com 100% de desconto
assert calcular_desconto(100, 100) == 0

# Produto com preço decimal
assert calcular_desconto(99.90, 10) == -89.91