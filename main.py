import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. {t['task']} [{status}]")

def mark_done(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True
        save_tasks(tasks)

tasks = load_tasks()

while True:
    print("\n1.Add 2.View 3.Mark Done 4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        mark_done(tasks)
    elif choice == '4':
        break
    else:
        print("Invalid choice")
