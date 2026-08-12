def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2




def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"




# Testes da função calcular_media
assert calcular_media(8, 6) == 7
assert calcular_media(10, 10) == 10
assert calcular_media(0, 0) == 0


# Testes da função verificar_situacao
assert verificar_situacao(7) == "Aprovado"
assert verificar_situacao(6) == "Aprovado"
assert verificar_situacao(5.9) == "Reprovado"


print("Todos os testes passaram!")

def verificar_situacao(media):
    # Garante que a média é válida antes de verificar
    assert 0 <= media <= 10, "A média deve estar entre 0 e 10!"
    
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

# Testes corrigidos
assert verificar_situacao(6) == "Aprovado", "Erro: O valor mínimo (6) deveria aprovar!"
assert verificar_situacao(5.9) == "Reprovado", "Erro: Notas abaixo de 6 devem reprovar!"

print("Função corrigida e testes passaram com sucesso!")

# O que acontece quando todos os testes passaram?
# programa executa todas as verificações do assert sem interromper a
# execução e imprime a mensagem print("Todos os testes passaram!"), 
# indicando que as funções estão funcionando conforme o esperado para os casos testados.

# Qual teste verifica o valor mínimo para aprovação? 
# O teste assert verificar_situacao(6) == "Aprovado"
# O 6 é a média para a verificação das notas se são maior ou
# menor que 6.

# Por que testar a nota 5.9 é importante? 
# Para garantir o comportamento do sistema logo abaixo da nota de corte (teste de limite/fronteira), 
# confirmando que a função retorna "Reprovado" corretamente para valores menores que 6.

#Altere temporariamente a função para considerar aprovado apenas quem obtiver média maior que 6. Qual teste falha? Explique por quê. 
# O teste assert verificar_situacao(6) == "Aprovado" falha. 
# Como a regra passa a exigir estritamente maior que 6 (> 6), 
# a média exata 6 não atende mais à condição e retorna "Reprovado".