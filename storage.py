import json
import shutil
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


def salvar_tarefas(tasks: list):
    """Salva as tarefas e alterações feitas no arquivo tasks.json.

    Args:
        tasks (list): Lista de tarefas a serem salvas. 
    """
    path = f"{os.getcwd()}/tasks.json"
    if os.path.exists(path):
        backup_file = path.replace(".json","_backup.json")
        shutil.copy(path, backup_file)
    
    with open("tasks.json", "w", encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


def pendentes_e_concluidas(tasks):
    pendentes = 0
    concluidas = 0
    for task in tasks:
        if task["status"] == "concluída":
            concluidas += 1
        else:
            pendentes += 1
    
    return pendentes, concluidas
            
