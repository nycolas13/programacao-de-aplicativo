id_funcionario = int(input("Digite seu ID: "))
temperatura = int(input("Digite a temperatura: "))
tempo = int(input("Digite o seu tempo: "))
if (id_funcionario % 3 == 0) and (temperatura > 40 or tempo > 8):
    print("Funcionário, você foi escalado para a manutenção preventia")
elif (temperatura < 40 or tempo < 8):
    print("O horário, sua máquina opera dento dos padrões normais")