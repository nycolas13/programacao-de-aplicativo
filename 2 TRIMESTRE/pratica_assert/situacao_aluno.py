def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"

# Média acima de 6
assert situacao_aluno(8) == "Aprovado"

# Média exatamente igual a 6
assert situacao_aluno(6) == "Aprovado"

# Média exatamente igual a 4
assert situacao_aluno(4) == "Recuperação"

# Média abaixo de 4
assert situacao_aluno(3) == "Reprovado"

# Média com decimal (5.9)
assert situacao_aluno(5.9) == "Recuperação"


