def buscar_tarefas(id: int, tasks: list) -> bool:
    """
    Verifica se uma tarefa com o ID especificado existe na lista de tarefas.

    Args:
        id (int): O ID da tarefa a ser buscada.
        tasks (list): Lista de dicionários representando tarefas.

    Returns:
        bool: True se a tarefa for encontrada, False caso contrário.
    """
    encontrada = False

    for task in tasks:
        if task["id"] == id:
            encontrada = True
            break
    
    return encontrada

def formatar_tarefa(id: int, status: str, descricao: str):
    """
    Exibe uma tarefa formatada na saída padrão.

    Args:
        id (int): ID da tarefa.
        status (str): Status da tarefa (pendente, concluída, etc.).
        descricao (str): Descrição da tarefa.
    """
    print(f"{id} {status} {descricao}")

def exibir_quantidades(pendentes, concluidas):
    """
    Exibe a quantidade de tarefas pendentes e concluídas.

    Args:
        pendentes (int): Número de tarefas pendentes.
        concluidas (int): Número de tarefas concluídas.
    """
    print_menu("ESTATÍSTICAS")
    print(f"Número de tarefas pendentes ❌: {pendentes}")
    print(f"Número de tarefas concluídas ✅: {concluidas}")

def input_inteiro(escolha: str) -> int:
    """
    Solicita ao usuário um número inteiro e trata erros de entrada.

    Args:
        escolha (str): Texto a ser exibido no prompt de entrada.

    Returns:
        int: Valor inteiro inserido pelo usuário.
    """
    try:
        valor = int(input(escolha))
        return valor
    except ValueError:
        print("Opção inválida. Digite um número inteiro.")

def print_menu(texto: str):
    """
    Exibe um menu com bordas estilizadas e texto centralizado.

    Args:
        texto (str): Texto a ser exibido no centro do menu.
    """
    width = 110
    border = "="*width
    empty_line = f"¦{' ' * (width - 2)}¦"
    print(border)
    print(empty_line)
    print(empty_line)
    print(f"¦{texto.center(width-2)}¦")
    print(empty_line)
    print(empty_line)
    print(border)

def msg_info(texto: str):
    """
    Exibe uma mensagem informativa com destaque.

    Args:
        texto (str): Mensagem a ser exibida.
    """
    print("\n" + "="*50)
    print(f"{texto}")
    print("="*50 + "\n")

def msg_alerta(texto: str):
    """
    Exibe uma mensagem de alerta com destaque.

    Args:
        texto (str): Mensagem de alerta.
    """
    print("\n" + "="*50)
    print(f"{texto}")
    print("="*50 + "\n")

def msg_erro(label: str):
    """
    Exibe uma mensagem de erro.

    Args:
        label (str): Texto do erro a ser exibido.
    """
    print(f"Erro inesperado: {label}")

def sem_tarefa():
    """
    Informa que não há tarefas armazenadas.
    """
    print("Não há tarefas armazenadas!")

def nao_encontrada():
     """
    Informa que a tarefa a ser removida não foi encontrada.
    """
     print("Não foi possível remover tarefa! Indíce inexistente.")

def opcoes_menu(modelo: str):
    """
    Exibe as opções do menu com base no modelo selecionado.

    Args:
        modelo (str): Tipo de menu ('principal' ou 'filtro').
    """
    if modelo == "principal":
        print("1️⃣  Adicionar tarefa")
        print("2️⃣  Listar tarefas")
        print("3️⃣  Concluir tarefa")
        print("4️⃣  Remover tarefa")
        print("5️⃣  Editar tarefa")
        print("6️⃣  Sair")
        print("=" * 50)
    elif modelo == "filtro":
        print("1️⃣  Todas")
        print("2️⃣  Pendentes")
        print("3️⃣  Concluídas")
        print("4️⃣  Voltar ao menu inicial")
