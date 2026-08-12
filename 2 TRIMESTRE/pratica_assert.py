# 1. Função para verificar se o número é par
def eh_par(numero):
    return numero % 2 == 0


# 2. Função para calcular o preço final com desconto
def calcular_desconto(preco, percentual):
    return preco - (preco * (percentual / 100))


# 3. Função para verificar a situação do voto no Brasil
def pode_votar(idade):
    if idade < 16:
        return "Não pode votar"
    elif (16 <= idade < 18) or (idade >= 70):
        return "Voto facultativo"
    else:
        return "Voto obrigatório"


# ==========================================
# TESTES PRÁTICOS (Com `assert`)
# ==========================================

# Testes para eh_par
# Verifica o comportamento com número par comum, ímpar comum e o zero (limite)
assert eh_par(4) is True, "Erro: 4 deveria ser par"
assert eh_par(3) is False, "Erro: 3 deveria ser ímpar"
assert eh_par(0) is True, "Erro: 0 deveria ser considerado par"

# Testes para calcular_desconto
# Verifica desconto padrão, desconto de 0% (limite) e desconto de 100% (limite)
assert calcular_desconto(200, 20) == 160, "Erro no cálculo de 20% de 200"
assert calcular_desconto(150, 0) == 150, "Erro: Desconto de 0% deve manter o preço"
assert calcular_desconto(80, 100) == 0, "Erro: Desconto de 100% deve zerar o preço"

# Testes para pode_votar (Regras do Brasil)
# Verifica caso comum de adulto, limite inferior para facultativo (16 anos) e proibido antes dos 16
assert pode_votar(25) == "Voto obrigatório", "Erro: 25 anos é voto obrigatório"
assert pode_votar(16) == "Voto facultativo", "Erro: 16 anos é voto facultativo"
assert pode_votar(15) == "Não pode votar", "Erro: 15 anos não pode votar"

print("Todos os testes do desafio passaram com sucesso!")
