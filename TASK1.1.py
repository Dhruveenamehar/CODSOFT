import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("To-Do List Application")
    print("----------------------")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print()

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, (task, status) in enumerate(tasks.items(), start=1):
            print(f"{index}. {task} - {'Completed' if status else 'Pending'}")
    print()

def add_task(tasks):
    task = input("Enter the new task: ")
    if task in tasks:
        print("Task already exists.")
    else:
        tasks[task] = False
        print("Task added successfully.")
    print()

def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to update: "))
    task_list = list(tasks.keys())
    if 0 < task_number <= len(task_list):
        task = task_list[task_number - 1]
        tasks[task] = not tasks[task]
        print("Task updated successfully.")
    else:
        print("Invalid task number.")
    print()

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    task_list = list(tasks.keys())
    if 0 < task_number <= len(task_list):
        task = task_list[task_number - 1]
        del tasks[task]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")
    print()

def main():
    tasks = {}
    while True:
        clear_screen()
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            clear_screen()
            view_tasks(tasks)
            input("Press Enter to return to the menu...")
        elif choice == '2':
            clear_screen()
            add_task(tasks)
            input("Press Enter to return to the menu...")
        elif choice == '3':
            clear_screen()
            update_task(tasks)
            input("Press Enter to return to the menu...")
        elif choice == '4':
            clear_screen()
            delete_task(tasks)
            input("Press Enter to return to the menu...")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
