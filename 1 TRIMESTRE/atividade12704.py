# O Conversor de Velocidade (Física Aplicada)
def converter_km_para_ms(velocidade):
    valor = velocidade / 3.6
    if valor > 80:
        print("REDUZA A VELOCIDADE")
        return valor
    elif valor < 80:
        return "segue viagem, senão a policia vem atrás"


velocidade = 80
usuario = int(input("Digite a velocidade do seu veículo:...... "))
mensagem_veiculo = converter_km_para_ms(usuario)
print(f"Equivale á {mensagem_veiculo}")


