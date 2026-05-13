lista_usuarios = ["admin", "convidado", "suporte", "teste"]

lista_usuarios.remove("teste")
del lista_usuarios[0:1]
print(f"Mostre como a lista ficou após as duas exclusões {lista_usuarios}.")