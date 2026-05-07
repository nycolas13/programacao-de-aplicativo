# Verificador de Paridade (Lógica Pura)
def eh_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

usuario = int(input("Digite um número: ")) 
mensagem = eh_par(usuario)
print(f"ESTE NÚMERO É: {mensagem}")
