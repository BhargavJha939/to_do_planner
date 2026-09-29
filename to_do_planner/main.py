from planner import print_tasks, show_alerts
from reports import build_report, export_report
from storage import load_tasks, save_tasks
from tasks import add_task, complete_task, delete_task, edit_task
from validators import ask_choice


def main():
    tasks = load_tasks()
    print("=" * 40 + "\n TO-DO PLANNER WITH DEADLINES\n" + "=" * 40)
    show_alerts(tasks)
    menu = {
        "1": ("Add task", add_task),
        "2": ("View all tasks", print_tasks),
        "3": ("View pending only", lambda t: print_tasks(t, True)),
        "4": ("Edit task", edit_task),
        "5": ("Mark task done", complete_task),
        "6": ("Delete task", delete_task),
        "7": ("Summary report", lambda t: print("\n" + build_report(t))),
        "8": ("Export report", export_report),
    }
    while True:
        print("\n" + "\n".join(f"  {k}. {v[0]}" for k, v in menu.items()) + "\n  9. Exit")
        choice = ask_choice("Enter choice (1-9): ", list(menu) + ["9"])
        if choice == "9":
            save_tasks(tasks)
            print("Goodbye!")
            break
        menu[choice][1](tasks)


if __name__ == "__main__":
    main()
