from banco import connect

def cadastrar_escolas(nome,cidade):
    assert nome.strip() != "", "O nome da escola não pode ser vazio."
    assert cidade.strip() != "", "A cidade não pode ser vazia."

    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO escolas(nome, cidade) VALUES (?,?)", (nome, cidade)) 
    conexao.commit()
    conexao.close()

def listar_escolas():
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM escolas")
    escolas = cursor.fetchall()
    conexao.close()
    return escolas