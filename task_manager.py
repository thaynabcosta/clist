from storage import salvar_tarefas, carregar_tarefas
from utils import buscar_tarefas

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
        print("Tarefa adicionada com sucesso!")
    except Exception as e:
        print("Erro inesperado ao tentar adicionar tarefa")



def remover(indice_tarefa: int):
    """Remove uma tarefa da lista conforme parâmetro passado

    Args:
        indice_tarefa (int): índice da tarefa a ser excluída
    """
    try:
        tasks = carregar_tarefas()
        encontrada = buscar_tarefas(indice_tarefa, tasks)
        
        for task in tasks:
            if task["id"] == indice_tarefa:
                tasks.remove(task)
                break

        if encontrada:
            salvar_tarefas(tasks)
            print("Tarefa removida com sucesso!")
        else:
            print("Não foi possível remover tarefa! Indíce inexistente.")
    except Exception as e:
        print(f"Erro inesperado ao tentar remover tarefa: {e}")
        

def listar():
    """Lista todas as tarefas armazenadas no arquivo tasks.json, mostrando seu ID e status
    """
    tasks = carregar_tarefas()
    for task in tasks:
        status_emoji = "✅" if task["status"] == "concluída" else "❌"
        print(f"{task["id"]} {status_emoji} {task["descricao"]}")


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
            print("Tarefa concluída com sucesso")
        else:
            print("Tarefa não encontrada!")

    except Exception as e:
        print(f"Erro inesperado ao tentar concluir tarefa: {e}")
    