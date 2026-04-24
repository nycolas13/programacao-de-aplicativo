#O Simulador de Batalha RPG (Escopo e Variáveis)
def sofrer_dano(dano,vida):
    while vida > 0:
        dano = vida - dano
        if dano > vida:
            return "GAME OVER"

valor_vida = 100
monstro = int(input("Digite o dano : "))   
        
jogador = 
mensagem = sofrer_dano(jogador)
print(mensagem)