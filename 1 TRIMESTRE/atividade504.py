#O Simulador de Batalha RPG (Escopo e Variáveis)
def sofrer_dano(dano,vida):
    while vida > 0:
        dano = vida - dano
        if dano > vida:
            return "GAME OVER"
        else:
            return "DERROTE O MONSTRO!!!"

valor_vida = 100  
personagem = int(input("Digite a quantidade de vida: ")) 
mensagem = sofrer_dano(personagem,valor_vida)
print(mensagem)