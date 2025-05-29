def buscar_tarefas(id, tasks):
    encontrada = False

    for task in tasks:
        if task["id"] == id:
            encontrada = True
            break
    
    return encontrada

def formatar_tarefa(id, status, descricao):
    print(f"{id} {status} {descricao}")

def exibir_quantidades(pendentes, concluidas):
    print("== E S T A T Í S T I C A S ==")
    print(f"Número de tarefas pendentes ❌: {pendentes}")
    print(f"Número de tarefas concluídas ✅: {concluidas}")

def input_inteiro(escolha: str) -> int:
    try:
        valor = int(input(escolha))
        return valor
    except ValueError:
        print("Opção inválida. Digite um número inteiro.")