import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect('pai_hospital.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS academia(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_unidade TEXT,
            bairro TEXT)''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            mensali INTEGER NOT NULL,
            id_academia INTEGER NOT NULL,
            FOREIGN KEY (id_academia) REFERENCES academia (id)
            )''')
        conexao.commit()

    except sqlite3.IntegrityError as e:
        print("ERROR: Algo que não existe: ",e)
    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
    except sqlite3.Error as e:
        print("ERROR: No SQL: ",e)
    finally:
        conexao.close()

def crair_alunos():
    try:
        conexao =  sqlite3.connect('pai_hospital.db')
        cursor = conexao.cursor()

        nome = input("Digite o seu nome: ")
        mensali = int(input("Digite a mensalidade: "))
        id_academia = int(input("Digite o ID da academia: "))

        cursor.execute('''
        INSERT INTO alunos(
        nome,mensali,id_academia) VALUES (?,?,?)''',(nome,mensali,id_academia))
        conexao.commit()
    except sqlite3.IntegrityError as e:
        print("ERROR: ",e)
    except sqlite3.Error as e:
        print("ERROR: ",e)
    conexao.close()

def criar_academia():
    conexao =  sqlite3.connect('pai_hospital.db')
    cursor = conexao.cursor()

    nome_unidade = input("Digite o nome: ")
    bairro = input("Digite o nome do bairro: ")

    cursor.execute('''
    INSERT INTO academia(
    nome_unidade,bairro) VALUES (?,?)''',(nome_unidade,bairro))

    conexao.commit()
    conexao.close()

criar_tabela()
crair_alunos()
criar_academia()