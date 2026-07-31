import sqlite3

def cadastrar_escola_manual():
    conexao = None
    try:
        id_escola = int(input("Digite o ID para a nova escola: "))
        nome = input("Nome da escola: ")

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO escolas (id, nome) VALUES (?,?)", (id_escola, nome))
        conexao.commit()
        print("Escola cadastrada com sucesso!")

    # 1. Trata erro de digitar letras onde deveria ser número
    except ValueError:
        print("Erro: O ID deve ser um número inteiro válido!")

    # 2. Trata a tentativa de inserir um ID que já existe no banco
    except sqlite3.IntegrityError:
        print(f"Erro: O ID já está cadastrado no sistema!")

    # 3. Trata outros erros genéricos de banco de dados
    except sqlite3.Error as e:
        print("Erro no banco de dados:", e)

    finally:
        # Garante o fechamento da conexão mesmo se der erro
        if conexao:
            conexao.close()

# Chamada da função para testar
cadastrar_escola_manual()