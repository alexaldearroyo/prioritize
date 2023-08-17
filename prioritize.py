# PRIORITIZE
# Shell script para añadir y manipular los quehaceres más prioritarios

import os


def show_tasks(tasks):
    print("-"*50)
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")


def add_task(tasks):
    task = input("\nEnter new priority: ")
    tasks.append(task)
    directory_path = os.path.expanduser("~/Library/Application Support/prioritize/")
    tasks_file_path = os.path.join(directory_path, "tasks.txt")

    with open(tasks_file_path, "a") as file:
        file.write(task + "\n")


def add_to_completed_file(task):
    directory_path = os.path.expanduser("~/Library/Application Support/prioritize/")
    completed_file_path = os.path.join(directory_path, "completed.txt")
    
    with open(completed_file_path, "a") as file:
        file.write(task + "\n")


def remove_from_tasks_file(tasks):
    directory_path = os.path.expanduser("~/Library/Application Support/prioritize/")
    tasks_file_path = os.path.join(directory_path, "tasks.txt")
    
    with open(tasks_file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def complete_task(tasks, completed):
    show_tasks(tasks)
    idx = int(input("\nEnter the number of completed priority: ")) -1
    if 0 <= idx < len(tasks):
        completed_task = tasks.pop(idx)
        completed.append(completed_task)
        add_to_completed_file(completed_task)
        remove_from_tasks_file(tasks)
    else:
        print("Invalid index.")


def show_completed(completed):
     print("Completed priorities: ")
     for task in completed:
        print(f"- {task}")

def clear_completed(completed): # Dar opcion que el usuario eliga el index de la tarea a eliminar
    directory_path = os.path.expanduser("~/Library/Application Support/prioritize/")
    completed_file_path = os.path.join(directory_path, "completed.txt")

    with open(completed_file_path, "w") as file:
        pass

    completed.clear()
    print("\nCompleted priorities cleared!")

def load_tasks():
    tasks = []
    completed = []

    directory_path = os.path.expanduser("~/Library/Application Support/prioritize/")
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    tasks_file_path = os.path.join(directory_path, "tasks.txt")
    completed_file_path = os.path.join(directory_path, "completed.txt")

    if not os.path.exists(tasks_file_path):
        with open(tasks_file_path, 'w') as file:
            pass
    else:
        with open(tasks_file_path, "r") as file:
            tasks = [line.strip() for line in file.readlines()]

    if not os.path.exists(completed_file_path):
        with open(completed_file_path, 'w') as file:
            pass
    else:
        with open(completed_file_path, "r") as file:
            completed = [line.strip() for line in file.readlines()]

    return tasks, completed

    
def main():
    tasks, completed = load_tasks()

    print("\n")
    print("P R I O R I T I Z E")

    if tasks:
        show_tasks(tasks)
    print("-"*50 + "\n")

    while True:
        print("a --- Add a priority")
        print("v --- Complete a priority")
        print("c --- Show completed priorities")
        print("o --- Clear completed priorities")
        print("x --- Exit program")
        if tasks:
            print("s --- Show priorities")
        option = input("\nChoose an option: ")

        if option == "s":
            show_tasks(tasks)
            print("-"*50 + "\n")
        elif option == "a":
            add_task(tasks)
            show_tasks(tasks)
            print("-"*50)
        elif option == "v":
            complete_task(tasks, completed)
            show_tasks(tasks)
            if tasks:
                print("-"*50)
        elif option == "c":
            print()
            print("-"*50)
            show_completed(completed)
            print("-"*50)
            print()
        elif option == "o":
            clear_completed(completed)
            print()
        elif option == "x":
            print("\nPriorities saved. See you next time!\n")
            break
        else:
            print("\nInvalid option. Please, choose a valid option.")

if __name__ == "__main__":
    main()


