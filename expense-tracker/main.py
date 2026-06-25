import storage, os
from expense import Expense
from functools import wraps

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pause_and_continue(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        clear_screen()
        result = func(*args,**kwargs)
        input("\nPress Enter to return to the main menu.")
        clear_screen()
        return result
    return wrapper

@pause_and_continue
def add_expense(expenses):
    amount = int(input("Enter Amount: ").strip())
    category = input("Enter Category: ").strip().lower()

    ex = Expense(category, amount)
    expenses.append(ex.to_dict())
    storage.save_expenses(expenses)
    print("Expense Added.")

@pause_and_continue
def view_expenses(expenses):
     for ex in expenses:
        print(Expense(ex["category"],ex["amount"]))

clear_screen()
print('*'*20, ' Expense Tracker ', '*'*20)

expenses = storage.load_expenses()

while True:
    
    print("""
1. Add Expense
2. View Expenses
3. Exit
""")
    
    try:
        choice = int(input("Enter your choice: ").strip())
    except ValueError:
        continue

    match choice:
        case 1:
            add_expense(expenses)

        case 2:
            view_expenses(expenses)
        
        case 3:
            print("exiting...")
            print("Program exited successfully")
            input("\nPress any key to close")
            clear_screen()
            break