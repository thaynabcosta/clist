from storage import salvar_tarefas

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

    if opcao == 1:
        tarefa_nova = input("Digite a tarefa: ")
        salvar_tarefas(tarefa_nova)

    elif opcao == 5:
        escolha = False