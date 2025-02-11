import json
import os

TODO_FILE = "todo_list.json"

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {"description": self.description, "completed": self.completed}

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(TODO_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task.to_dict())
        self.save_tasks()
        print(f"✅ Úloha \"{description}\" bola pridaná.")

    def list_tasks(self):
        if not self.tasks:
            print("📂 Žiadne úlohy.")
        else:
            print("\n📋 Zoznam úloh:")
            for idx, task in enumerate(self.tasks, 1):
                status = "✅ Dokončená" if task["completed"] else "❌ Nedokončená"
                print(f"{idx}. {task['description']} - {status}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print(f"🎯 Úloha \"{self.tasks[index]['description']}\" je dokončená.")
        else:
            print("❌ Neplatné číslo úlohy.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f"🗑️ Úloha \"{removed_task['description']}\" bola vymazaná.")
        else:
            print("❌ Neplatné číslo úlohy.")

def main():
    todo = TodoList()

    while True:
        print("\n📝 TO-DO LIST")
        print("1 Pridať úlohu")
        print("2 Zobraziť úlohy")
        print("3 Označiť úlohu ako dokončenú")
        print("4 Vymazať úlohu")
        print("5 Ukončiť")

        choice = input("👉 Vyber možnosť: ")

        if choice == "1":
            description = input("Zadaj popis úlohy: ")
            todo.add_task(description)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            todo.list_tasks()
            index = int(input("Zadaj číslo úlohy na dokončenie: ")) - 1
            todo.complete_task(index)
        elif choice == "4":
            todo.list_tasks()
            index = int(input("Zadaj číslo úlohy na vymazanie: ")) - 1
            todo.delete_task(index)
        elif choice == "5":
            print("👋 Ukončujem program.")
            break
        else:
            print("❌ Neplatná voľba. Skús znova.")

if __name__ == "__main__":
    main()
