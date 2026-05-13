# Filtro Avançado de Candidatos (RH)
def verificar_aprovacao(nota_teste,anos_xp,possui_certificado):
    if nota_teste > 80 and (anos_xp > 2 or possui_certificado == "S"):
        return "Contratar"
    else:
        return "Descartar"
        
nota = int(input("digite sua nota de teste: "))
ano = int(input("digite quantos anos de seus estudos: "))
certificado = input("digite se vc possui certificado (S/N): ")
mensagem = verificar_aprovacao(nota,ano,certificado)
print(mensagem)