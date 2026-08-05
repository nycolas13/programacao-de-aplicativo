import sqlite3


def criar_tabela():
    try:
        conexao = sqlite3.connect('pai_hospitais.db')
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hospitais(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cidade TEXT
            )''')
       
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crm TEXT UNIQUE NOT NULL,
                id_hospital INTEGER NOT NULL,
                FOREIGN KEY (id_hospital) REFERENCES hospitais (id)
                )''')
        
        conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro no ID de hospital não existe")
    except ValueError:
        print("Erro o ID tentativa de transformar ID em texto")
    except sqlite3.Error:
        print('Erro no sqlite')
    finally:
        conexao.close()

criar_tabela()

def criar_medicos():
    try:
        conexao = sqlite3.connect('pai_hospitais.db')
        cursor = conexao.cursor()

        nome_medico = input("Digite o nome: ")
        crm = int(input("Digite o CRM: "))
        id_hospital = int(input("Digite o ID do hospital: "))

        cursor.execute('''
            INSERT INTO medicos(
                nome,crm, id_hospital) VALUES(?,?,?)''',(nome_medico,crm,id_hospital))

        conexao.commit()
        print(f"Médico {nome_medico} cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print(f"Error: O hospital com o ID {id_hospital} não existe (ou o CRM já foi cadastrado)")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar médico: {e}")

criar_medicos()

def criar_hospital():
    
        conexao = sqlite3.connect('pai_hospitais.db')
        cursor = conexao.cursor()

        nome = input("Digite um nome: ")
        cidade = input("Digite o nome da cidade: ")

        cursor.execute(''' INSERT INTO hospitais(
                       nome, cidade) VALUES (?,?)''', (nome,cidade))
        
        conexao.commit()
        print(f"Médico {nome} cadastrado com sucesso")

        conexao.close()
criar_hospital()
    

        
