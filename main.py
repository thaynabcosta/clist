from task_manager import adicionar, remover, listar, concluir, editar

def menu():
    """Exibição do Menu
    """
    print(" == M E N U ==")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Editar tarefa")
    print("6. Sair")


def main():

    menu()

    #Escolha do usuário
    escolha = True
    while escolha:
        try:
            opcao = int(input("Escolha: "))

            if opcao == 1:
                nova_tarefa = input("Digite a tarefa: ")
                adicionar(nova_tarefa)
            
            elif opcao == 2:
                listar()

            elif opcao == 3:
                indice_tarefa = int(input("Digite o índice da tarefa que deseja concluir: "))
                concluir(indice_tarefa)


            elif opcao == 4:
                tarefa_removida = int(input("Digite o índice da tarefa a ser removida: "))
                remover(tarefa_removida)

            elif opcao == 5:
                tarefa_editada = int(input("Digite o índice da tarefa a ser editada: "))
                nova_descricao = input("Digite a atualização: ")
                editar(tarefa_editada, nova_descricao)

            elif opcao == 6:
                escolha = False
                
            
        except ValueError:
            print("Opção inexistente. Tente um número entre 1 e 5")

        menu()

        
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro: {e}")

       