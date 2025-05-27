from storage import salvar_tarefas, carregar_tarefas
import json

def adicionar(descricao: str):
    """Adiciona uma nova tarefa à lista existente e salva no arquivo 'tasks.json'

    Args:
        descricao (str): descrição da tarefa a ser adicionada
    """
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


def remover(indice_tarefa: int):
    """Remove uma tarefa da lista conforme parâmetro passado

    Args:
        indice_tarefa (int): índice da tarefa a ser excluída
    """
    tasks = carregar_tarefas()
    for task in tasks:
        if task["id"] == indice_tarefa:
            tasks.remove(task)
            break
    salvar_tarefas(tasks)
        

def listar():
    """Lista todas as tarefas armazenadas no arquivo tasks.json, mostrando seu ID e status
    """
    tasks = carregar_tarefas()
    for task in tasks:
        status_emoji = "✅" if task["status"] == "concluída" else "❌"
        print(f"{task["id"]} {status_emoji} {task["descricao"]}")


def concluir():
    pass
