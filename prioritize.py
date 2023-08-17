# PRIORITIZE
# Shell script para añadir y manipular los quehaceres más prioritarios

import os

# Constants
DIRECTORY_PATH = os.path.expanduser("~/Library/Application Support/prioritize/")
TASKS_FILE_PATH = os.path.join(DIRECTORY_PATH, "tasks.txt")
COMPLETED_FILE_PATH = os.path.join(DIRECTORY_PATH, "completed.txt")

# Ensure the directory exists
if not os.path.exists(DIRECTORY_PATH):
    os.makedirs(DIRECTORY_PATH)


# Display the current tasks in a numbered list with formatting.
def show_tasks(tasks):
    print("-"*50)
    for idx, task in enumerate(tasks, 1):
        print(f"\033[1m\033[30m\033[43m{idx}. {task}\033[0m")

# Add a new task to the list and save it to the tasks.txt file.
def add_task(tasks):
    task = input("\nEnter new priority: ")
    tasks.append(task)
    tasks_file_path = TASKS_FILE_PATH

    with open(tasks_file_path, "a") as file:
        file.write(task + "\n")

# Add a completed task to the completed.txt file.
def add_to_completed_file(task):
    
    with open(COMPLETED_FILE_PATH, "a") as file:
        file.write(task + "\n")

# Rewrite the tasks.txt file with the current tasks.
def remove_from_tasks_file(tasks):
    
    with open(TASKS_FILE_PATH, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Mark a task as completed, remove it from tasks, and add it to completed.
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

# Display the completed tasks.
def show_completed(completed):
     print("Completed priorities: ")
     for task in completed:
        print(f"- {task}")

# Clear all completed tasks from the list and the completed.txt file.
def clear_completed(completed): # Dar opcion que el usuario eliga el index de la tarea a eliminar

    with open(COMPLETED_FILE_PATH, "w") as file:
        pass

    completed.clear()
    print("\n*** Completed priorities cleared ***")

# Load tasks and completed tasks from their respective files.
def load_tasks():
    tasks = []
    completed = []

    if not os.path.exists(DIRECTORY_PATH):
        os.makedirs(DIRECTORY_PATH)

    if not os.path.exists(TASKS_FILE_PATH):
        with open(TASKS_FILE_PATH, 'w') as file:
            pass
    else:
        with open(TASKS_FILE_PATH, "r") as file:
            tasks = [line.strip() for line in file.readlines()]

    if not os.path.exists(COMPLETED_FILE_PATH):
        with open(COMPLETED_FILE_PATH, 'w') as file:
            pass
    else:
        with open(COMPLETED_FILE_PATH, "r") as file:
            completed = [line.strip() for line in file.readlines()]

    return tasks, completed

    
def main():
    tasks, completed = load_tasks()

    print("\n")
    print("P R I O R I T I Z E")

    if tasks:
        show_tasks(tasks)
    print("-"*50)

    while True:
        print("a --- Add a priority")
        if tasks:
            print("v --- Complete a priority")
        if completed:
            print("c --- Show completed priorities")
            print("o --- Clear completed priorities")
        if tasks:
            print("s --- Show priorities")
        print("x --- Exit program")
    
        option = input("\nChoose an option: ")

        if option == "s":
            print()
            show_tasks(tasks)
            print("-"*50 + "\n")
        elif option == "a":
            add_task(tasks)
            show_tasks(tasks)
            print("-"*50)
        elif option == "v":
            complete_task(tasks, completed)
            print()
            print("*** Task completed ***")
            show_tasks(tasks)
            if tasks:
                print("-"*50)
        elif option == "c":
            print()
            print("-"*50)
            show_completed(completed)
            print("-"*50)
        elif option == "o":
            clear_completed(completed)
            print("-"*50)
        elif option == "x":
            print("\nPriorities saved. See you next time!\n")
            break
        else:
            print("\nInvalid option. Please, choose a valid option.\n")

if __name__ == "__main__":
    main()


