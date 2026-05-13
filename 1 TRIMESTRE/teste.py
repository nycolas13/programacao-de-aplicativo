senha_correta = "sei lá"
def validar_senha(senha, senha_correta):
    while senha != senha_correta:
        print("senha incorreta")
        senha = input("digite a senha: ")
    if senha == senha_correta:
        print("bem-vindo")
senha_usuario = input("digite a senha nova: ")
validar_senha(senha_usuario, senha_correta)