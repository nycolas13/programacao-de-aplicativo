import sqlite3

#Inicialização do Banco
def criar_tabela():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreing_keys = ON; ")

        cursor.execute("DROP TABLE IF EXISTS hoteis;")
        cursor.execute("DROP TABLE IF EXISTS quartos;")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hoteis(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cidade TEXT)''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quartos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL,
            preco_diaria INTEGER NOT NULL,
            id_hoteis INTEGER NOT NULL,
            FOREIGN KEY (id_hoteis) REFERENCES hoteis(id))''')
        
        conexao.commit()

    except sqlite3.IntegrityError as e:
        print("ERROR: ID não existe: ",e)
    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
    except sqlite3.Error as e:
        print("ERROR: No SQL: ",e)
    finally:
        conexao.close()
criar_tabela()

#Cadastro com Validação
def criar_quarto():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        numero = int(input("Digite um número: "))
        preco_diaria = int(input("Digite o preço diario: "))
        id_hoteis= int(input("Digite o ID do Hotel: "))

        cursor.execute('''INSERT INTO quartos(
        numero,preco_diaria,id_hoteis) VALUES (?,?,?)''',(numero,preco_diaria,id_hoteis))

        conexao.commit()

    except sqlite3.IntegrityError as e:
        print("ERROR: ",e)
    except ValueError as e:
        print("ERROR: ",e)
    except sqlite3.Error as e:
        print("ERROR: ",e)
    finally:
        conexao.close()

def criar_hotel():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        nome = input("Digite um nome: ")
        cidade = input("Digite o nome da cidade: ")
        
        cursor.execute('''
        INSERT INTO hoteis(nome,cidade) VALUES(?,?)''',(nome,cidade))
        
        conexao.commit()

    except sqlite3.IntegrityError as e:
        print("ERROR: ",e)
    except ValueError as e:
        print("ERROR: ", e)
    except sqlite3.Error as e:
        print("ERROR: ",e)
    finally:
        conexao.close()

opcao = 0

while opcao != 3:
    print("1-Cadastrar quarto | 2-Identificar o hotel | 3-Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_quarto()
    elif opcao == "2":
        criar_hotel()
    elif opcao == "3":
        break
print("FECHANDO....")
