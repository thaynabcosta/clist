def buscar_tarefas(id, tasks):
    encontrada = False

    for task in tasks:
        if task["id"] == id:
            encontrada = True
            break
    
    return encontrada