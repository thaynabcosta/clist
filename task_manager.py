from storage import salvar_tarefas, carregar_tarefas, pendentes_e_concluidas
from utils import *

def adicionar(descricao: str):
    """Adiciona uma nova tarefa à lista existente e salva no arquivo 'tasks.json'

    Args:
        descricao (str): descrição da tarefa a ser adicionada
    """
    try:
        tasks = carregar_tarefas()

        ids = [t['id'] for t in tasks]
        proximo_id = max(ids) + 1 if ids else 1

        nova_tarefa = {
            "id": proximo_id,
            "descricao": descricao,
            "status": "pendente"
        }
        tasks.append(nova_tarefa)
        salvar_tarefas(tasks)
        msg_info("Tarefa adicionada com sucesso!")
    except Exception as e:
        msg_erro(e)



def remover(indice_tarefa: int):
    """Remove uma tarefa da lista conforme parâmetro passado

    Args:
        indice_tarefa (int): índice da tarefa a ser excluída
    """
    try:
        tasks = carregar_tarefas()
        encontrada = buscar_tarefas(indice_tarefa, tasks)
        
        for i, task in enumerate(tasks):
            if task["id"] == indice_tarefa:
                del tasks[i]
                break

        if encontrada:
            salvar_tarefas(tasks)
            msg_info("Tarefa removida com sucesso!")
        else:
            msg_alerta("Não foi possível remover tarefa! Insira um índice válido.")
    except Exception as e:
        msg_erro(e)
        

def listar(filtro: int):
    """Lista todas as tarefas armazenadas no arquivo tasks.json, mostrando seu ID e status
    """
    try:
        tasks = carregar_tarefas()

        if tasks != []:
            if filtro == 1: 
                print_menu("TODAS AS TAREFAS")
                for task in tasks:
                    status_emoji = "✅" if task["status"] == "concluída" else "❌"
                    formatar_tarefa(task["id"], status_emoji, task["descricao"])

                tasks_pendentes, tasks_concluidas = pendentes_e_concluidas(tasks)
                exibir_quantidades(tasks_pendentes, tasks_concluidas)

            elif filtro == 2:
                print_menu("TAREFAS PENDETES")
                for task in tasks:
                    if task["status"] == "pendente":
                        status_emoji = "❌"
                        formatar_tarefa(task["id"], status_emoji, task["descricao"])
                    
            elif filtro == 3:
                print_menu("TAREFAS CONCLUÍDAS")
                for task in tasks:
                    if task["status"] == "concluída":
                        status_emoji = "✅"
                        formatar_tarefa(task["id"], status_emoji, task["descricao"])
        else:
            msg_alerta("Nenhuma tarefa na memória.")

    except Exception as e:
        msg_erro(e)

def concluir(indice_task:int):
    """Concluí tarefas a partir de um índice, alterando seu status de "pendente" para "concluída"

    Args:
        indice_task (int): índice da tarefa a ser concluída
    """
    try: 
        tasks = carregar_tarefas()
        encontrada = buscar_tarefas(indice_task, tasks)

        for task in tasks:
            if task.get("id") == indice_task:
                task["status"] = "concluída"
                break
        
        if encontrada:
            salvar_tarefas(tasks)
            msg_info("Tarefa concluída com sucesso!")
        else:
            msg_alerta("Não foi possível concluir tarefa!Insira um índice válido.")

    except Exception as e:
        msg_erro(e)
    
def editar(indice, nova_descricao):
        
    try:
        tasks = carregar_tarefas()
        encontrada = buscar_tarefas(indice, tasks)
        
        for task in tasks:
            if task["id"] == indice:
                task["descricao"] = nova_descricao
                break

        if encontrada:
            salvar_tarefas(tasks)
            msg_info("Tarefa editada com sucesso!")

        else:
            msg_alerta("Não foi possível editar tarefa!Insira um índice válido.")
    
    except Exception as e:
        msg_erro()
            