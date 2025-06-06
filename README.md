# CLIST - Gerenciador de Tarefas em Linha de Comando

CLIST é uma ferramenta de linha de comando simples e poderosa para criação, organização e visualização de listas de tarefas diretamente no terminal.

## 🚀 Recursos/ Funcionalidaes

- 📋 Criação de tarefas
- ✅ Marcação de tarefas como concluídas
- 🔍 Filtro por status
- 💾 Persistência local em arquivo JSON
- 🖥️ Interface de terminal amigável

## 🏗️ Status do Projeto

✅ Concluído | Pronto para uso

## 🛠️ Como Usar / Instalar

### Pré-requisitos
- Python 3.12+
- pip

### Instalação
```bash
git clone https://github.com/thaynabcosta/clist.git
cd clist
pip install -r requirements.txt
python clist.py
```

## 💡 Exemplos de Uso

### Adicionar Tarefa

Menu inicial
![Menu Inicial](docs/imagens/menu_inicial.png)

Escolhendo a função adicionar
![Adicionar](docs/imagens/escolha_adicionar.png)

Digitando nova tarefa
![Digitando tarefa](docs/imagens/digitar_tarefa.png)

Tarefa adicionada com sucesso! Retorna o menu principal
![Mensagem de sucesso ao adicionar tarefa](docs/imagens/tarefa_adicionada_com_sucesso.png)

### Listar Tarefas

Escolhendo opção 2 para listar tarefas
![Escolha Listar](docs/imagens/escolha_listar.png)

Menu filtro de exibição
![Escolha Filtro](docs/imagens/escolha_filtro.png)

Listar todas as tarefas
![Escolha Todas as Tarefas](docs/imagens/filtro_todas_tarefas.png)

Exibição apenas de tarefas pendentes
![Escolha tarefas pendentes](docs/imagens/exibicao_tarefas_pendentes.png)

Exibição apenas de tarefas concluídas
![Escolha tarefas concluídas](docs/imagens/exibicao_tarefas_concluidas.png)

### Concluir Tarefas

Escolhendo a opção 3 para concluir tarefas
![Escolha concluir tarefas](docs/imagens/escolha_concluir.png)

Digitar índice atribuído à tarefa na lista
![Digitando índice da tarefa](docs/imagens/concluindo_tarefa.png)

### Editar Tarefas

Escolhendo a opção 5 para editar tarefas
![Escolha editar tarefas](docs/imagens/escolha_editar.png)

Digitando o índice da tarefa a ser editada, em seguida escrevendo a alteração
![Editando tarefa](docs/imagens/editando_tarefa.png)

### Remover Tarefas

Escolhendo a opção 4 para remover tarefas
![Escolha remover](docs/imagens/escolha_remover.png)

Em seguida, digitando o índice da tarefa para excluir
![Remover](docs/imagens/remover_tarefa.png)

## 🧱 Tecnologias Utilizadas

- Python 3.12+
- JSON (para armazenamento local)

## 📁 Estrutura de Pastas

clist/  
├── .gitignore  
├── main.py  
├── README.py  
├── storage.py  
├── task_manager.py  
├── tasks.json  
└── utils.py  

## 👩‍💻 Contribuições

Contribuições são bem-vindas! Para isso:
- Faça um fork
- Crie uma branch com sua feature (`git checkout -b feature/xyz`)
- Faça commit das mudanças (`git commit -m 'feat: xyz'`)
- Faça push para a branch (`git push origin feature/xyz`)
- Abra um Pull Request

## 📜 Licença

Este projeto está licenciado sob a [Licença MIT](./LICENSE). © 2025 Bia
