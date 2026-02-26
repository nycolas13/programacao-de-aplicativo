idade = int (input ("Digite sua idade: "))
saldo_da_carteira = float (input ("Digite o seu saldo: "))

if idade >= 18 and saldo_da_carteira >= 50.0:
    print("Acesso autorizado! Bem-vindo ao evento")

elif idade < 18 and saldo_da_carteira < 50.0:
    print("Infelizmente você não cumpre os requisitos de entrada")