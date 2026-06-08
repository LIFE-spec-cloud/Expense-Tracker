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