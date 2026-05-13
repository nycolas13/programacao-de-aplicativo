usuario = (input("Digite o usuário: "))
codigo_secreto = int (input("Digite o código: "))

if usuario == "admin" and codigo_secreto == 125:
    print("Acesso ao servidor liberado. Sistema online")
elif usuario != "admin" and codigo_secreto != 125:
    print("Falha na autentificação. Alerta de segurança ligado!")