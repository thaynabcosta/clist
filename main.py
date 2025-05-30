from task_manager import adicionar, remover, listar, concluir, editar
from utils import *

def mostrar_menu_principal():
    print_menu("MENU")
    opcoes_menu("principal")

def mostrar_menu_filtro():
    print_menu("FILTRO")
    opcoes_menu("filtro")

def main():

    #Escolha do usuário
    while True:
            mostrar_menu_principal()
            try:
                opcao = input_inteiro("Escolha: ")

                if opcao == 1:
                    nova_tarefa = input("Digite a tarefa: ")
                    adicionar(nova_tarefa)
                
                elif opcao == 2:
                    try:                
                        while True:
                            mostrar_menu_filtro()
                            filtro = input_inteiro("Digite o índice do filtro desejado: ")
                            if filtro in [1, 2, 3]:
                                listar(filtro)
                            elif filtro == 4:
                                break
                            else:
                                print("Digite um valor válido[1-4]:")
                    except Exception as e:
                        msg_erro(e)

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
                    break    
                else: 
                    msg_alerta("Opção inexistente!")
            except Exception as e:
                msg_erro(e)

        
if __name__ == "__main__":
    main()

       