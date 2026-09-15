import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect("reservas.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            solicitante TEXT NOT NULL,
            laboratorio TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def menu():
    inicializar_banco()
    
    laboratorios = {
        1: "Laboratório de Informática 01",
        2: "Laboratório de Informática 02",
        3: "Laboratório de Robótica",
        4: "Laboratório de Eletroeletrônica"
    }

    while True:
        print("\n--- SISTEMA DE RESERVAS ---")
        print("1. Realizar Reserva")
        print("2. Consultar Reservas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                print("\nLaboratórios disponíveis:")
                for k, v in laboratorios.items():
                    print(f"{k} - {v}")
                
                lab_num = int(input("Escolha o número do laboratório: "))
                if lab_num not in laboratorios:
                    print("Erro: Laboratório inválido.")
                    continue
                
                laboratorio = laboratorios[lab_num]
                solicitante = input("Nome do solicitante: ")
                data = input("Data (DD/MM/AAAA): ")
                horario = input("Horário (HH:MM): ")

                # Validações com assert
                assert solicitante.strip() != "", "O solicitante não pode ser vazio."
                assert data.strip() != "", "A data não pode ser vazia."
                assert horario.strip() != "", "O horário não pode ser vazio."

                conexao = sqlite3.connect("reservas.db")
                cursor = conexao.cursor()
                
                # Verifica conflito
                cursor.execute("""
                    SELECT * FROM reservas 
                    WHERE laboratorio = ? AND data = ? AND horario = ?
                """, (laboratorio, data, horario))
                
                if cursor.fetchone():
                    print("\nAviso: Conflito detectado! Laboratório já reservado neste horário.")
                else:
                    cursor.execute("""
                        INSERT INTO reservas (solicitante, laboratorio, data, horario) 
                        VALUES (?, ?, ?, ?)
                    """, (solicitante, laboratorio, data, horario))
                    conexao.commit()
                    print("Reserva cadastrada com sucesso!")
                
                conexao.close()

            elif opcao == "2":
                print("\n--- LISTA DE RESERVAS ---")
                conexao = sqlite3.connect("reservas.db")
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM reservas")
                reservas = cursor.fetchall()
                conexao.close()

                if not reservas:
                    print("Nenhuma reserva encontrada.")
                else:
                    for r in reservas:
                        print(f"ID: {r[0]} | Solicitante: {r[1]} | Lab: {r[2]} | Data: {r[3]} | Horário: {r[4]}")

            elif opcao == "3":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

        except ValueError:
            print("Erro: Digite um valor numérico válido.")
        except AssertionError as e:
            print(f"Erro de validação: {e}")
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")


menu()
    

