import sqlite3

#Inicialização do Banco
def criar_tabela():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreing_keys = ON; ")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hoteis(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cidade TEXR)''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quarto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL,
            preco_diaria INTEGER NOT NULL,
            id_hotel,
            FOREING KEY (id_hoteis) REFERENCES hoteis(id))''')
        conexao.commit()

    except sqlite3.IntegrityError as e:
        print("ERROR: ID não existe: ",e)
    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
    except sqlite3.Error as e:
        print("ERROR: No SQL: ",e)
    finally:
        conexao.close()

#Cadastro com Validação
def criar_quarto():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        numero = int(input("Digite um número: "))
        preco_diaria = int(input("Digite o preço diario: "))
        id_hotel = int(input("Digite o ID do Hotel: "))

        cursor.execute('''INSERT INTO quarto(
        numero,preco_diaria,id_hotel) VALUES (?,?,?)''',(numero,preco_diaria,id_hotel))

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
        