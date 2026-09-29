import os
from datetime import date

from config import REPORT_FILE
from planner import status_of


def build_report(tasks):
    done = sum(t["done"] for t in tasks)
    overdue = sum(1 for t in tasks if not t["done"] and status_of(t).startswith("OVERDUE"))
    pct = done / len(tasks) * 100 if tasks else 0
    return (f"TO-DO REPORT ({date.today()})\n{'=' * 30}\nTotal tasks : {len(tasks)}\n"
            f"Completed   : {done} ({pct:.0f}%)\nPending     : {len(tasks) - done}\nOverdue     : {overdue}")


def export_report(tasks):
    try:
        os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
        with open(REPORT_FILE, "w") as f:
            f.write(build_report(tasks))
        print(f"Report saved to {REPORT_FILE}")
    except OSError as e:
        print(f"[Error] Could not write report: {e}")
