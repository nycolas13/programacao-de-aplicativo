import sqlite3

def criar_tabela():

    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fabricantes_globais(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca_eletronica TEXT,
            origem TEXT
            )''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posto_atendimento(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_equipe TEXT NOT NULL,
            id_fabricante INTEGER NOT NULL,
            FOREIGN KEY (id_fabricante) REFERENCES fabricantes_globais(id)
            )''')
        conexao.commit()
    except sqlite3.IntegrityError as e:
        print("ERROR: O ID não existe: ",e)
    except ValueError as e:
        print("ERROR: Tentativa de transformar o ID em texto: ",e)
    except sqlite3.Error as e:
        print("ERROR: ERRO NO SQL: ",e)
    finally:
        conexao.close()
criar_tabela()

def cadastrar_fabricante():
    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()

        marca = input("Digite a marca do eletrônico: ")
        origem = input("Digite a origem do fabricante: ")

        cursor.execute('''
            INSERT INTO fabricantes_globais(
            marca,origem) VALUES(?,?)''',(marca,origem))
        conexao.commit()
        print("Salvo")
    except sqlite3.IntegrityError as e:
        print("ERROR: O ID não existe: ",e)
    except ValueError as e:
        print("ERROR: Tentativa de transformar o ID em texto: ",e)
    finally:
        conexao.close()
cadastrar_fabricante()

def listar_fabricante():
    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM fabricantes_globais")
        registro = cursor.fetchall()

        print("\n--- Lista de Fabricantes Globais ---")
        if not registro:
            print("Nenhum fabricante cadastrado")
        for reg in registro:
            print(f"ID: {reg[0]} | Marca: {reg[1]} | Origem: {reg[2]}")
    except sqlite3.Error as e:
        print("Error: na lista",e)
    finally:
        conexao.close()
listar_fabricante()

def atualizar_fabricante():
    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()

        id_reg = int(input("Digite o ID do fabricante que deseja atualizar: "))

        cursor.execute("SELECT id FROM fabricantes_globais WHERE id = ?", (id_reg,))
        if not cursor.fetchone():
            print("ID do fabricante não encontrado")
        
        nova_marca = input("Digite a nova marca do elerônico: ")
        nova_origem = input("Digite a nova origem: ")

        if not nova_marca or not nova_origem:
            print("Os campos não pode ser vazios")

        cursor.execute("UPDATE fabricantes_globais SET marca_eletronica = ?, origem = ? WHERE id =?",(nova_marca, nova_origem, id_reg))
        conexao.commit()
        print("Fabricante atualizado com sucesso!")

    except ValueError as e:
        print("ERROR: DIGITE UM NÚMERO INTEIRO")
    except sqlite3.Error as e:
        print("ERROR: ATUALIZAR")
    finally:
        conexao.close()
atualizar_fabricante()

def excluir_fabricante():
    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()

        listar_fabricante()
        id_reg = int(input("Digite o ID do fabricante que deseja excluir: "))

        cursor.execute("SELECT id FROM posto_atendimento WHERE id_fabricante = ?",(id_reg,))

        if cursor.fetchall():
            print("Erro: Existem postos de atendimento vinculados a este fabricante."
          " Exclua-os primeiro.")
            
        cursor.execute("DELETE FROM fabricantes_globais WHERE id = ? ",(id_reg,))
        conexao.commit()
        print("Fbricantes excluido com sucesso!")

    except ValueError as e:
        print("Entrada inválida. Digite um número inteiro")
    except sqlite3.Error as e:
        print(f"ERROR ao excluir: ",e)
    finally:
        conexao.close()
excluir_fabricante()

def cadastrar_posto():
    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()

        nome_equipe = input("Digite o nome da sua equipe de fabricantes: ")
        id_fabricante = int(input("Digite o ID do Fabricante: "))

        cursor.execute("INSERT INTO posto_atendimento(nome_equipe,id_fabricante) VALUES (?,?)",(nome_equipe,id_fabricante))
        conexao.commit()
        print("Salvo")
    except sqlite3.IntegrityError as e:
        print("ERROR: ID não existe")
    except ValueError as e:
        print("ERROR:Tentativa de transformar o ID em texto: ",e)
    finally:
        conexao.close()
cadastrar_posto()

def listar_posto():
    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM posto_atendimento")
        registro = cursor.fetchall()

        print("\n--- Lista de Posto de Atendimento ---")
        if not registro:
            print("Nenhum posto de atendimento cadastrado")
        for reg in registro:
            print(f"ID: {reg[0]} | Cidade: {reg[1]} | Fabricante Vincular: {reg[2]}")
    except sqlite3.Error as e:
        print("Error: na lista",e)
    finally:
        conexao.close()
listar_posto()

def atualizar_posto():
    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()

        listar_posto()
        id_reg = int(input("Digite o ID do posto de atendimento que deseja atualizar: "))

        cursor.execute("SELECT id FROM posto_atendimento WHERE id = ? ",(id_reg,))
        if not cursor.fetchone():
            print("ID do posto de atendimento não encontrado.")
        listar_fabricante()
        novo_id_fabricante = int(input("Digite o novo ID do Fabricante Correspondente: "))
        cursor.execute("SELECT id FROM fabricantes_globais WHERE id = ?",(novo_id_fabricante))
        nova_cidade = input("Digite a nova cidade: ")
        if not nova_cidade:
            print("A cidade não pode ser vazia.")

        cursor.execute("UPDATE posto_atendimento SET cidade = ?, id_fabricante = ? WHERE id = ?",(nova_cidade, novo_id_fabricante, id_reg))
        conexao.commit()
        print("Posto de atendimento atualizado com sucesso!")
    except ValueError as e:
        print("Entrada inválida. Digite um número inteiro.",e)
    except sqlite3.Error as e:
        print("ERROR: AO ATUALIZAR",e)
    finally:
        conexao.close()
atualizar_posto()

def excluir_posto():
    try:
        conexao = sqlite3.connect('sistema_assistencia.db')
        cursor = conexao.cursor()
        
        listar_posto()
        id_reg = int(input("DIGITE o ID do posto de atendimento que deseja excluir: "))

        cursor.execute("DELETE FROM posto_atendimento WHERE id = ?",(id_reg))
        conexao.commit()
        print("Posto de atendimento excluido com sucesso!")
    except ValueError as e:
        print("Entrada inválida. Digite um número inteiro.")
    except sqlite3.Error as e:
        print("ERROR: ao excluir",e)
    finally:
        conexao.close()
excluir_posto()

def menu():
    opcao = 9
    while opcao != 9:
        print("1-Cadastar Fabricante | " \
        "2 - Listar Fabricante | 3 - Atualizar Fabricante |" \
        "4 - Excluir Fabricante")
        print("5 - Cadastrar Posto de Atendimento |" \
        "6 - Listar Posto de Atendimento | 7 - Atualizar Posto de Atendimento |" \
        "8 - Excluir Posto de Atendimento | 9 - SAIR")

        try:
            opcao = (input("Escolha uma opção: "))

            if opcao == "1":
                cadastrar_fabricante()
            elif opcao == "2":
                listar_fabricante()
            elif opcao == "3":
                atualizar_fabricante()
            elif opcao == "4":
                excluir_fabricante()
            elif opcao == "5":
                cadastrar_posto()
            elif opcao == "6":
                listar_posto()
            elif opcao == "7":
                atualizar_posto()
            elif opcao == "8":
                excluir_posto()
            elif opcao == "9":
                print("Saindo")
                break
            else:
                print("Opção inválida! Escolha um número inteiro entre 9 e 8.")
        except ValueError as e:
            print("ERROR: Digite apenas números inteiros válidos.")
if __name__ == "__main__":
    menu()
