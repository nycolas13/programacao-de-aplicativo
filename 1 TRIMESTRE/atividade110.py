# pate1
id_do_usuario = int (input("Digite seu ID: "))
valor_compra = float (input("Digite o valor: R$ "))

# parte 2
if id_do_usuario % 2 == 0 and valor_compra > 500.00:
    print("PARÁBENS! Você ganhou um cupom para sua compra")
    
else: 
    print("Obrigado pela compra,. Continue acompanhando nossas promoções!")
    