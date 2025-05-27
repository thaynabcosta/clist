from task_manager import adicionar, remover, listar, concluir

def menu():
    """Exibição do Menu
    """
    print(" == M E N U ==")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")


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
                escolha = False

            elif opcao > 5:
                print("Opção inxistente. Tente outra entre [1-5]")
            
        except ValueError:
            print("Opção inexistente. Tente um número entre 1 e 5")


if __name__ == "__main__":
    
    main()
    

       