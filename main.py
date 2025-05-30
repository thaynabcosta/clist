from task_manager import adicionar, remover, listar, concluir, editar
from utils import input_inteiro, print_menu

def menu():
    """Exibição do Menu
    """
    print_menu("MENU PRINCIPAL")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Editar tarefa")
    print("6. Sair")

def menu_listagem():
    """Exibição do Menu de Filtros
    """
    print("===============================")
    print("¦        FILTRO TAREFAS       ¦")
    print("===============================")
    print("1. Todas")
    print("2. Pendentes")
    print("3. Concluídas")
    print("4. Voltar ao menu inicial")

def main():

    menu()

    #Escolha do usuário
    escolha = True
    while escolha:
    
        opcao = input_inteiro("Escolha: ")

        if opcao == 1:
            nova_tarefa = input("Digite a tarefa: ")
            adicionar(nova_tarefa)
        
        elif opcao == 2:
            escolha_filtro = True
            try:                
                while escolha_filtro:
                    menu_listagem()
                    filtro = input_inteiro("Digite o índice do filtro desejado: ")
                    if filtro == 1:
                        listar(filtro)
                    elif filtro == 2:
                        listar(filtro)
                    elif filtro == 3:
                        listar(filtro)
                    elif filtro == 4:
                        escolha_filtro = False
                    else:
                        print("Digite um valor válido[1-4]:")
            except Exception as e:
                print(f"Erro inesperado ao selecionar filtro de listagem: {e}")

        elif opcao == 3:
            indice_tarefa = input_inteiro("Digite o índice da tarefa que deseja concluir: ")
            concluir(indice_tarefa)


        elif opcao == 4:
            tarefa_removida = input_inteiro("Digite o índice da tarefa a ser removida: ")
            remover(tarefa_removida)

        elif opcao == 5:
            tarefa_editada = input_inteiro("Digite o índice da tarefa a ser editada: ")
            nova_descricao = input("Digite a atualização: ")
            editar(tarefa_editada, nova_descricao)

        elif opcao == 6:
            escolha = False
            break    
        else: 
            print("Opção inexistente!")

        menu()

        
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro: {e}")

       