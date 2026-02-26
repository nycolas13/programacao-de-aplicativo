nivel_atual = int (input("qual seu nível?: "))
quantidade_de_esferas = int (input("quantas esferas você coletou?: "))

if nivel_atual >= 20 and quantidade_de_esferas > 50:
    print("Habilidade Super Salto desbloqueado")
elif quantidade_de_esferas < 20 and nivel_atual < 50:
    print("Requisitos insuficientes para nova habilidade")