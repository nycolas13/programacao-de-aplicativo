from banco import criar_tabela
import escola, turma, aluno
import sqlite3

def menu():
    criar_tabela()
    opcao = "0"

    while opcao != "7":
        print("\n--- GESTÃO ESCOLAR ---")
        print("1. Cadastrar Escola | 2. Listar Escolas")
        print("3. Cadastrar Turma  | 4. Listar Turmas")
        print("5. Cadastrar Aluno  | 6. Listar Alunos")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome da escola: ")
                cidade = input("Cidade: ")
                escola.cadastrar_escola(nome, cidade)
                print("Escola cadastrada com sucesso!")
                
            elif opcao == "2":
                for e in escola.listar_escolas():
                    print(f"ID: {e[0]} | Nome: {e[1]} | Cidade: {e[2]}")
                    
            elif opcao == "3":
                nome_t = input("Nome da turma: ")
                id_esc = int(input("ID da escola vinculada: "))
                turma.cadastrar_turma(nome_t, id_esc)
                print("Turma cadastrada com sucesso!")
                
            elif opcao == "4":
                for t in turma.listar_turmas():
                    print(f"ID: {t[0]} | Turma: {t[1]} | ID Escola: {t[2]}")
                    
            elif opcao == "5":
                nome_a = input("Nome do aluno: ")
                idade = int(input("Idade: "))
                id_t = int(input("ID da turma vinculada: "))
                aluno.cadastrar_aluno(nome_a, idade, id_t)
                print("Aluno cadastrado com sucesso!")
                
            elif opcao == "6":
                for a in aluno.listar_alunos():
                    print(f"ID: {a[0]} | Nome: {a[1]} | Idade: {a[2]} | ID Turma: {a[3]}")
                    
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
                
        except ValueError:
            print("Erro: Digite um valor numérico válido para IDs ou idades.")
        except AssertionError as ae:
            print(f"Erro de validação: {ae}")
        except sqlite3.Error as se:
            print(f"Erro no Banco de Dados: Verifique se o ID vinculado realmente existe. ({se})")

menu()