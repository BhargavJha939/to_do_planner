from datetime import datetime


def ask_choice(prompt, valid):
    while True:
        c = input(prompt).strip()
        if c in valid:
            return c
        print("Invalid choice. Options:", ", ".join(valid))


def ask_text(prompt):
    while True:
        t = input(prompt).strip()
        if t:
            return t
        print("This field cannot be empty.")


def ask_date(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt).strip(), "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("Use format YYYY-MM-DD, e.g. 2026-10-15.")
