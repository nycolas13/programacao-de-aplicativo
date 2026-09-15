def busca_nome(lista, nome):
    for i in range(len(lista)):
        if lista[i].lower() == nome.lower():
            return f"Encontrado na posição {i}!"
    return "Nome não encontrado."

alunos = ["Ana", "Carlos", "Beatriz", "Daniel"]
print(busca_nome(alunos, "Beatriz"))