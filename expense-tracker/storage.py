import json

def save_expenses(expense):
    with open("expenses.json", 'w') as f:
        json.dump(expense, f, indent=4)

def load_expenses(expenses_file="expenses.json"):
    try:
        with open(expenses_file, 'r') as f:
            expenses = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        expenses = []
    return expenses
