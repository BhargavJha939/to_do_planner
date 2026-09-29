import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "tasks.json")
REPORT_FILE = os.path.join(BASE_DIR, "data", "todo_report.txt")

PRIORITIES = {"1": "High", "2": "Medium", "3": "Low"}
DUE_SOON_DAYS = 2  # tasks due within this many days get a reminder
