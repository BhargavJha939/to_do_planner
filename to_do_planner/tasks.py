from config import PRIORITIES
from storage import save_tasks
from validators import ask_choice, ask_date, ask_text


def create_task(tasks, title, due, priority):
    next_id = max([t["id"] for t in tasks], default=0) + 1
    task = {"id": next_id, "title": title, "due": due, "priority": priority, "done": False}
    tasks.append(task)
    return task


def find_task(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None


def ask_id(tasks, prompt):
    raw = input(prompt).strip()
    found = [t for t in tasks if str(t["id"]) == raw]
    if not found:
        print("No task with that ID.")
    return found[0] if found else None


def add_task(tasks):
    title = ask_text("Task title: ")
    due = ask_date("Due date (YYYY-MM-DD): ")
    pri = ask_choice("Priority (1=High 2=Medium 3=Low): ", list(PRIORITIES))
    t = create_task(tasks, title, due, int(pri))
    save_tasks(tasks)
    print(f"Added task #{t['id']}.")


def edit_task(tasks):
    t = ask_id(tasks, "Enter task ID to edit: ")
    if not t:
        return
    print("Leave title blank to keep it.")
    t["title"] = input(f"Title [{t['title']}]: ").strip() or t["title"]
    if input("Change due date? (y/n): ").strip().lower() == "y":
        t["due"] = ask_date("New due date (YYYY-MM-DD): ")
    save_tasks(tasks)
    print("Task updated.")


def complete_task(tasks):
    t = ask_id(tasks, "Enter task ID to mark done: ")
    if t:
        t["done"] = True
        save_tasks(tasks)
        print("Marked as done.")


def delete_task(tasks):
    t = ask_id(tasks, "Enter task ID to delete: ")
    if t:
        tasks.remove(t)
        save_tasks(tasks)
        print("Deleted.")
