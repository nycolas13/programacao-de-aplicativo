import sqlite3

nome_serie = input("Digite um nome: ")
id_escola = int(input("Digite o ID: "))

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None
    try:
        conexao = sqlite3.connect('/ pasta_protegida/sistema.db')
        with conexao:
           cursor = conexao.cursor()
           cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome, id_escola))

           
    except sqlite3.Error as e:
        print("Erro técnicos:", e) 
    finally:
        if conexao:
            conexao.close()

# Para corrigir usaremos o "with", o código dentro do with roda sem erros. O Python faz o conexao.commit() automaticamente ao sair do bloco with.
# Como o valor None não é uma conexão aberta, ele não possui o método .close(). A conexão como None tem que ser colocada antes do try 
# e colocar um if conexao: dentro do finally antes de tentar fechar!
cadastrar_serie_seguro(nome_serie, id_escola)