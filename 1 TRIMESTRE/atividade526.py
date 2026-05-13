compras = [""]
item = ""
while item != "fim":
    item = input("produto: ")
    if item != "fim":
        compras.append(item)
for produto in compras:
    print(produto)