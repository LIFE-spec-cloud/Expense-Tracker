import json
from datetime import datetime

DATA_FILE = "expenses.json"


def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
        
def add_expense():

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    print("\nCategories:")
    print("Food")
    print("Transport")
    print("Entertainment")
    print("Other")

    category = input("Enter category: ").strip()

    valid_categories = [
        "Food",
        "Transport",
        "Entertainment",
        "Other"
    ]

    if category not in valid_categories:
        print("Invalid category.")
        return

    note = input("Enter note (optional): ")

    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

def main():
    
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter By Category")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "4":
            break

if __name__ == "__main__":
    main()