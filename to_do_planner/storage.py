import json
import os

from config import DATA_FILE


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except (json.JSONDecodeError, OSError):
        print("[Warning] Saved tasks unreadable. Starting fresh.")
    return []


def save_tasks(tasks):
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
    except OSError as e:
        print(f"[Error] Could not save: {e}")
