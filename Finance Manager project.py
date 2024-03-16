

def add_expense(expenses, category, amount ):
    category=category.lower()
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def sub_expense(expenses, category, amount):
    category.lower()
    if category in expenses:
        expenses[category] -= amount
    else:
        print(f"No expenses found for category: {category}")

def view_expenses(expenses):
    total_expense = 0
    print("Category\tAmount")
    print("=====================")
    for category, amount in expenses.items():
        print(f"{category}\t\t{amount}")
        print(total_expense )
    print("=====================")
    print(f"Total Expense:\t{total_expense}")

def main():
    expenses = {}
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Remove Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, amount)
            print("Expense added successfully!")
        elif choice == '2':
            if not expenses:
                print("No expenses recorded yet!")
            else:
                view_expenses(expenses)
        elif choice == '3':
            category = input("Enter expense category: ")
            category.lower()
            amount = float(input("Enter expense amount: "))
            sub_expense(expenses, category, amount)
            total_expense=total_expense-amount
            print("Expense removed successfully.!")
        elif choice == '4':
            print("Exiting...")
            print("This Finance manager is made by Aaryan Khandelwal")
            print("Thank you, Please come again")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
