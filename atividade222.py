# Validador de Senha (Segurança)
senha = "LAGAPT"
def senhar_valida (senha):
    while senha != 6:
        print("Senha Incorreta !")
        senha = input("Escreva a senha denovo: ")
    if senha == 6:
        return "Senha cadastrada com sucesso!"
usuario = input("Digite sua senha: ")
mensagem = senhar_valida(usuario)
print(mensagem)
    
