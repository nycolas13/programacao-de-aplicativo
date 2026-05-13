ano_do_usuario = float (input("Digite o ano que você nasceu: "))

if (ano_do_usuario % 4 != 0 and ano_do_usuario % 100) or (ano_do_usuario % 400 == 0):
    print("O ano {ano_do_usuario} é bissexto!") 
else:
    print("O ano {ano_do_usuario} é um ano comum")