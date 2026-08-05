import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect('pai_hospitais.db')
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cinema(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cinema TEXT,
            shopping TEXT)''')
        
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS salas(
                numero_sala TEXT NOT NULL,
                capacidade INTEGER,
                id_cinema INTEGER NOT NULL,
                FOREIGN KEY (id_cinema) REFERENCES cinema (id)
                       )''')
        conexao.commit()
    except sqlite3.IntegrityError as e:
        print("ERROR: O ID de cinema não existe: ",e)
    except ValueError as e:
        print("ERROR: Tentativa de transformar o ID em texto: ",e)
    except sqlite3.Error as e:
        print("ERROR: Tem algum erro no SQL: " ,e)
    finally:
        conexao.close()
criar_tabela()



def criar_salas():
    try:
        conexao = sqlite3.connect('pai_hospitais.db')
        cursor = conexao.cursor()

        numero_sala = input("Digite o nome da sala: ")
        capacidade = int(input("Digite a quantidade de assentos para as pessoas: "))
        id_cinema = int(input("Digite o ID do cinema: "))

        cursor.execute('''
            INSERT INTO salas(numero_sala, capacidade, id_cinema) VALUES (?,?,?)''',(numero_sala,capacidade,id_cinema))
        
        conexao.commit()
        print("Cadastrado")
    except sqlite3.IntegrityError as e:
        print("ERROR: o ID não existe: ",e)
    except sqlite3.Error as e:
        print("ERROR: NO CADASTRO: ",e)

criar_salas()

def criar_cinema():
    
    conexao = sqlite3.connect('pai_hospitais.db')
    cursor = conexao.cursor()

    nome_cinema = input("Digite o nome do cinema: ")
    shopping = input("Digite o nome do shopping: ")
    

    cursor.execute('''
        INSERT INTO cinema(nome_cinema,shopping) VALUES (?,?)''', (nome_cinema, shopping))

    conexao.commit()
    print("Salvando ")
    conexao.close()

criar_cinema()
