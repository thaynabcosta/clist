import json
import os

def carregar_tarefas():
    """ Carrega e retorna a lista de tarefas do arquivo 'tasks.json'.
    
    Returns:
        list: Lista de tarefas carregadas. Retorna uma lista vazia caso o arquivo não exista
        ou esteja vazio/inválido.
    """
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def salvar_tarefas(nova_tarefa: str):
    """Adiciona uma nova tarefa à lista existente e salva no arquivo 'tasks.json'.

    Args:
        nova_tarefa (str): A tarefa que será adicionada à lista.
    """
    tasks = carregar_tarefas()
    tasks.append(nova_tarefa)
    with open("tasks.json", "w", encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
