# Exibição do Menu
print(" == M E N U ==")
print("1. Adicionar tarefa")
print("2. Listar tarefas")
print("3. Concluir tarefa")
print("4. Remover tarefa")
print("5. Sair")

#Escolha do usuário
escolha = True
while escolha:
    opcao = int(input("Escolha: "))

    if opcao == 5:
        escolha = False