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

# O que acontece quando todos os testes passaram?
# programa executa todas as verificações do assert sem interromper a
# execução e imprime a mensagem print("Todos os testes passaram!"), 
# indicando que as funções estão funcionando conforme o esperado para os casos testados.

# Qual teste verifica o valor mínimo para aprovação? 
# O teste assert verificar_situacao(6) == "Aprovado"
# O 6 é a média para a verificação das notas se são maior ou
# menor que 6.

# or que testar a nota 5.9 é importante? 
# Para garantir o comportamento do sistema logo abaixo da nota de corte (teste de limite/fronteira), 
# confirmando que a função retorna "Reprovado" corretamente para valores menores que 6.