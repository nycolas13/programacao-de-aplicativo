# Transferencia de arquivo
pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"] 
concluidos = []
concluidos.append(pendentes[0])
pendentes.pop(0)
print(f"Arquivo novo trocado {pendentes} e {concluidos}")