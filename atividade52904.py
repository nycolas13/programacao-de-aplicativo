def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    return f"RUA...{rua}, NÚMERO...{numero}, BAIRRO...{bairro}, CIDADE...{cidade}, CEP...{cep}"

etiqueta = gerar_etiqueta("Av. Paulista", "1000", "Bela Vista", "São Paulo", "01310-100")
print(etiqueta)