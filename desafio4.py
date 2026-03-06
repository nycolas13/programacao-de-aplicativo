# parte 1
codigo_drone = int(input("Digite o código: "))
autorizacao = input("Possui Autorização da Torre? (S/N): ")

# parte 2 análise de pouso
if(codigo_drone == 999 or autorizacao == "S"):
    bateria = int (input("Qual seu nivel de bateria (0 a 100): "))
    clima = input("ENSOLARADO ou CHUVOSO?: ")
    velocidade_do_vento = int(input("Qual é a velocidade do vento (Km/h): "))
    if bateria < 10:
        print("AUTORIZAÇÃO IMEDIATAMENTE!")
    elif bateria >= 10:
        if (clima == "ENSOLARADO" and velocidade_do_vento < 30) or (clima == "CHUVOSO" and velocidade_do_vento < 10):
            print("POUSO AUTORIZADO: Iniciando descida.")
        else:
            print("POUSSO NEGADO: Condições meterológicas perigosos. Aguarde em órbita.")
else:
    print("ACESSO NEGADO")
   

