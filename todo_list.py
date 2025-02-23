import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Carrega as tarefas do arquivo."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Salva as tarefas no arquivo."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def list_tasks():
    """Lista todas as tarefas."""
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa pendente!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Adiciona uma nova tarefa."""
    task = input("Digite a nova tarefa: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Tarefa adicionada!")

def complete_task():
    """Marca uma tarefa como concluída."""
    tasks = load_tasks()
    list_tasks()
    try:
        index = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Tarefa concluída e removida!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

def main():
    """Loop principal do programa."""
    while True:
        print("\n1. Listar Tarefas\n2. Adicionar Tarefa\n3. Concluir Tarefa\n4. Sair")
        choice = input("Escolha uma opção: ")
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
