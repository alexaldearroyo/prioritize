# PRIORITIZE
# Shell script para añadir y manipular los quehaceres más prioritarios

import os

def show_tasks(tasks):
    print("\nPriorities TO-DO:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def add_task(tasks):
    task = input("\nEnter new priority: ")
    tasks.append(task)

def complete_task(tasks, completed):
    show_tasks(tasks)
    idx = int(input("\nEnter the number of completed priority: ")) -1
    if 0 <= idx < len(tasks):
            completed.append(tasks.pop(idx))
    else:
        print("Invalid index.")

def show_completed(completed):
     print("\nCompleted priorities: ")
     for task in completed:
        print(f"- {task}")

def clear_completed(completed): # Dar opcion que el usuario eliga el index de la tarea a eliminar
    completed.clear()
    print("\nCompleted priorities cleared\n")

def save_tasks(tasks, completed):
    with open("priorities.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

    with open("completed.txt", "w") as file:
        for task in completed:
                file.write(task + "\n")

def load_tasks():
    tasks = []
    completed = []

    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
             tasks = [line.strip() for line in file.readlines()]

    if os.path.exists("completed.txt"):
         with open("completed.txt", "r") as file:
              completed = [line.strip() for line in file.readlines()]

    return tasks, completed

def main():
    tasks, completed = load_tasks()

    print("\n")
    print(" ____  ____  __  __  ____  __  ____  __  ____  ____")
    print("(  _ \(  _ \(  )/  \(  _ \(  )(_  _)(  )(__  )(  __)")
    print(" ) __/ )   / )((  O ))   / )(   )(   )(  / _/  ) _) ")
    print("(__)  (__\_)(__)\__/(__\_)(__) (__) (__)(____)(____)")
    print("\n")

    while True:
       
        print("1. Show priorities")
        print("2. Add priority")
        print("3. Mark priority as completed")
        print("4. Show completed priorities")
        print("5. Clear completed priorities") #posiblemente cambiar a poder eliminarlas una por una
        print("6. Exit and save")
        option = input("\nChoose an option: ")

        if option == "1":
            show_tasks(tasks)
            print()
        elif option == "2":
            add_task(tasks)
            print()
        elif option == "3":
            complete_task(tasks, completed)
        elif option == "4":
            show_completed(completed)
            print()
        elif option == "5":
            clear_completed(completed)
            print()
        elif option == "6":
            save_tasks(tasks, completed)
            print("\nPriorities saved. See you next time!\n")
            break
        else:
            print("\nInvalid option. Please, choose a valid option.")

if __name__ == "__main__":
    main()


