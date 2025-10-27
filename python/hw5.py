# Simple To-Do List
# Allows the user to:
# 1. Add a new task
# 2. View tasks
# 3. Delete a task by name or number
# 4. Quit the program

from typing import List


def show_menu() -> None:
    print("\nMenu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks: List[str]) -> None:
    task: str = input("Enter new task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append(task)
    print(f"Added: '{task}'")


def view_tasks(tasks: List[str]) -> None:
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")


def delete_task(tasks: List[str]) -> None:
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    choice = input("Enter task number or name to delete: ").strip()

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: '{removed}'")
        else:
            print("Invalid task number.")
        return

    if choice in tasks:
        tasks.remove(choice)
        print(f"Removed: '{choice}'")
    else:
        print("Task not found.")


def main() -> None:
    tasks: List[str] = []
    while True:
        show_menu()
        option = input("Choose (1-4): ").strip()

        if option == "1":
            add_task(tasks)
        elif option == "2":
            view_tasks(tasks)
        elif option == "3":
            delete_task(tasks)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
