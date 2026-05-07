def contar_caracteres(frase):
    if len(frase) < 5:
        return "Nome de usuário muito curto"
    else:
        return "Nome aceito"
usuario = input("Digite um nome de usuário: ")
mensagem = contar_caracteres(usuario)
print(mensagem)