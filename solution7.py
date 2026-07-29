def show_menu():
    """Display the menu options."""
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """Prompt for a task description and add it to the list."""
    description = input("Enter task: ")
    tasks.append(description)
    print(f'Task added: "{description}"')


def view_tasks(tasks):
    """Display all tasks, numbered from 1. Show a message if empty."""
    if not tasks:
        print("Your task list is empty!")
        return
    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    """Show tasks, ask for a number to remove, and delete it."""
    if not tasks:
        print("Your task list is empty! Nothing to delete.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to delete: ")

    if not choice.isdigit():
        print("Error: Please enter a valid task number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Error: That task number doesn't exist.")
        return

    removed = tasks.pop(index)
    print(f'Task "{removed}" has been removed.')


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a number between 1 and 4.")

        print()  # blank line for readability between menu cycles


if __name__ == "__main__":
    main()