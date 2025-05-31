from storage import salvar_tarefas, carregar_tarefas, pendentes_e_concluidas, gerar_prox_id
from utils import *

def adicionar(descricao: str):
    """Adiciona uma nova tarefa à lista existente e salva no arquivo 'tasks.json'

    Args:
        descricao (str): descrição da tarefa a ser adicionada
    """
    try:
        if not descricao.strip():
            msg_alerta("A descrição da tarefa não pode ser vazia!")
            return
        
        tasks = carregar_tarefas()
        id = gerar_prox_id(tasks)

        nova_tarefa = {
            "id": id,
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
        tarefa = next((t for t in tasks if t["id"] == indice_tarefa), None)

        if tarefa is None:
            msg_alerta("Tarefa com ID inserido não encontrada.")
        
        tasks.remove(tarefa)
        salvar_tarefas(tasks)
        msg_info("Tarefa removida com sucesso!")
    
    except Exception as e:
        msg_erro(e)
        

def listar(filtro: int):
    """Lista todas as tarefas armazenadas no arquivo tasks.json, mostrando seu ID e status
    """
    try:
        tasks = carregar_tarefas()

        if not tasks:
            msg_alerta("Nenhuma tarefa na memória!")

        titulos = {1:"TODAS AS TAREFAS", 2:"TAREFAS PENDENTES", 3:"TAREFAS CONCLUÍDAS"}
        print_menu(titulos.get(filtro, "LISTA DE TAREFAS"))

        for task in tasks:
            status = task["status"]
            status_emoji = "✅" if status == "concluída" else "❌" 

            if filtro == 1:
                formatar_tarefa(task["id"], status_emoji, task["descricao"])
            elif filtro == 2 and status == "pendente":
                formatar_tarefa(task["id"], status_emoji, task["descricao"])
            elif filtro == 3 and status == "concluída":
                formatar_tarefa(task["id"], status_emoji, task["descricao"])

        if filtro == 1:
            tasks_pendentes, tasks_concluidas = pendentes_e_concluidas(tasks)
            exibir_quantidades(tasks_pendentes, tasks_concluidas)

    except Exception as e:
        msg_erro(e)

def concluir(indice_task:int):
    """Concluí tarefas a partir de um índice, alterando seu status de "pendente" para "concluída"

    Args:
        indice_task (int): índice da tarefa a ser concluída
    """
    try: 
        tasks = carregar_tarefas()

        if not tasks:
            msg_alerta("Não foi possível concluir tarefa!Insira um índice válido.")

        for task in tasks:
            if task.get("id") == indice_task:
                task["status"] = "concluída"
                salvar_tarefas(tasks)
                msg_info("Tarefa concluída com sucesso!")
                break
            else:
                msg_alerta("Tarefa não pôde ser concluída! Índice inexistente.")
        

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
            