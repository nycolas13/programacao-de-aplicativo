import sqlite3

def buscar_prfessor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM professores WHERE id = ?",(id_prof,))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()

# O erro ocorre por causa da falta da virgula no (id_prof),para sqlite entender que não é apenas uma instring, mas uma Tupla. 