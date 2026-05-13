lista_nomes = ["Nycolas","JU","Nathaly","Keeast"]
nomes_escolhidos = [""]
# Use o for e um if 
for nome in lista_nomes:
    if len(nome) > 5:
        nomes_escolhidos.append(nome)
        print(f"Apenas nomes de 5 letras. {nome}")
         
   