from datetime import date, datetime

from config import DUE_SOON_DAYS, PRIORITIES


def status_of(t):
    if t["done"]:
        return "DONE"
    days = (datetime.strptime(t["due"], "%Y-%m-%d").date() - date.today()).days
    if days < 0:
        return f"OVERDUE by {-days}d"
    if days == 0:
        return "DUE TODAY"
    return f"due in {days}d" if days <= DUE_SOON_DAYS else "upcoming"


def sorted_view(tasks, only_pending=False):
    shown = [t for t in tasks if not (only_pending and t["done"])]
    return sorted(shown, key=lambda t: (t["done"], t["due"], t["priority"]))


def print_tasks(tasks, only_pending=False):
    rows = sorted_view(tasks, only_pending)
    if not rows:
        print("\nNo tasks to show.")
        return
    print(f"\n{'ID':<4}{'Title':<25}{'Due':<12}{'Priority':<10}Status")
    print("-" * 65)
    for t in rows:
        print(f"{t['id']:<4}{t['title'][:24]:<25}{t['due']:<12}{PRIORITIES[str(t['priority'])]:<10}{status_of(t)}")


def overdue_and_due_soon(tasks):
    pending = [t for t in tasks if not t["done"]]
    overdue = [t for t in pending if status_of(t).startswith("OVERDUE")]
    soon = [t for t in pending if status_of(t).startswith(("DUE", "due"))]
    return overdue, soon


def show_alerts(tasks):
    overdue, soon = overdue_and_due_soon(tasks)
    if overdue:
        print(f"[ALERT] {len(overdue)} overdue task(s): " + ", ".join(t["title"] for t in overdue))
    if soon:
        print(f"[Reminder] {len(soon)} task(s) due within {DUE_SOON_DAYS} days: " + ", ".join(t["title"] for t in soon))
