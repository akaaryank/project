class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.total_expense = 0

    def add_expense(self, category, amount):
        try:
            category = category.lower()
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            if category in self.expenses:
                self.expenses[category] += amount
            else:
                self.expenses[category] = amount
            self.total_expense += amount
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def remove_expense(self, category, amount):
        try:
            category = category.lower()
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            if category in self.expenses:
                if self.expenses[category] < amount:
                    raise ValueError("Insufficient funds in the category.")
                self.expenses[category] -= amount
                self.total_expense -= amount
                print("Expense removed successfully!")
            else:
                print(f"No expenses found for category: {category}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_expenses(self):
        try:
            if not self.expenses:
                raise ValueError("No expenses recorded yet!")
            print("Category\tAmount")
            print("=====================")
            for category, amount in self.expenses.items():
                print(f"{category}\t\t{amount}")
            print("=====================")
            print(f"Total Expense:\t{self.total_expense}")
        except ValueError as e:
            print(f"Error: {e}")

    def category_percentages(self):
        try:
            if not self.expenses:
                raise ValueError("No expenses recorded yet!")
            print("Category\tPercentage")
            print("=====================")
            for category, amount in self.expenses.items():
                percentage = (amount / self.total_expense) * 100
                print(f"{category}\t\t{percentage:.2f}%")
            print("=====================")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    expense_tracker = ExpenseTracker()

    print("Welcome to Finance Manager")

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Remove Expense")
        print("4. Category Percentages")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            expense_tracker.add_expense(category, amount)
        elif choice == '2':
            expense_tracker.view_expenses()
        elif choice == '3':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            expense_tracker.remove_expense(category, amount)
        elif choice == '4':
            expense_tracker.category_percentages()
        elif choice == '5':
            print("Exiting...")
            print("This Finance manager is made by Aaryan Khandelwal")
            print("Thank you, Please come again")
            break
        else:
            print("Invalid choice. Please try again.")

main()

