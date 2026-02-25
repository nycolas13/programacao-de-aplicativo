ataque_do_heroi = int (input("dano de ataque: "))
defesa_do_vilao = int (input("defesa do vilão: "))

dano = ataque_do_heroi - defesa_do_vilao

if ataque_do_heroi > defesa_do_vilao:
    print("Ataque crítico, você causou dano ao vilão!")
elif defesa_do_vilao > ataque_do_heroi:
    print("O vilão bloqueiou o ataque!")
