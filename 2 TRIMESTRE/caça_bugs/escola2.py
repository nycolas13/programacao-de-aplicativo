import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,))

    conexao.commit()
    conexao.close()
# o ERRO ESTAVA NO "where id = ?" antes (WHERE id = id_escola) o que causa um incomodo no sqlite
deletar_escola_antiga()