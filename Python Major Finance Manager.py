import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.total_expense = 0

    def add_expense(self, category, amount):
        category = category.lower()
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.total_expense += amount

    def remove_expense(self, category, amount):
        category = category.lower()
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if category in self.expenses:
            if self.expenses[category] < amount:
                raise ValueError("Insufficient funds in the category.")
            self.expenses[category] -= amount
            self.total_expense -= amount
        else:
            raise ValueError("No expenses found for this category.")

    def get_expenses(self):
        return self.expenses

    def category_percentages(self):
        percentages = {}
        for category, amount in self.expenses.items():
            percentages[category] = (amount / self.total_expense) * 100
        return percentages

class ExpenseTrackerGUI:
    def __init__(self, root, tracker):
        self.tracker = tracker
        self.root = root
        self.root.title("Expense Tracker")

        self.add_frame = tk.Frame(root)
        self.add_frame.pack(pady=10)
        
        tk.Label(self.add_frame, text="Category:").grid(row=0, column=0, padx=5)
        self.category_entry = tk.Entry(self.add_frame)
        self.category_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(self.add_frame, text="Amount:").grid(row=0, column=2, padx=5)
        self.amount_entry = tk.Entry(self.add_frame)
        self.amount_entry.grid(row=0, column=3, padx=5)
        
        tk.Button(self.add_frame, text="Add Expense", command=self.add_expense).grid(row=0, column=4, padx=5)

        self.remove_frame = tk.Frame(root)
        self.remove_frame.pack(pady=10)
        
        tk.Label(self.remove_frame, text="Category:").grid(row=0, column=0, padx=5)
        self.remove_category_entry = tk.Entry(self.remove_frame)
        self.remove_category_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(self.remove_frame, text="Amount:").grid(row=0, column=2, padx=5)
        self.remove_amount_entry = tk.Entry(self.remove_frame)
        self.remove_amount_entry.grid(row=0, column=3, padx=5)
        
        tk.Button(self.remove_frame, text="Remove Expense", command=self.remove_expense).grid(row=0, column=4, padx=5)

        self.view_frame = tk.Frame(root)
        self.view_frame.pack(pady=10)
        
        tk.Button(self.view_frame, text="View Expenses", command=self.view_expenses).grid(row=0, column=0, padx=5)
        tk.Button(self.view_frame, text="Category Percentages", command=self.view_category_percentages).grid(row=0, column=1, padx=5)

    def add_expense(self):
        try:
            category = self.category_entry.get()
            amount = float(self.amount_entry.get())
            self.tracker.add_expense(category, amount)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.category_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def remove_expense(self):
        try:
            category = self.remove_category_entry.get()
            amount = float(self.remove_amount_entry.get())
            self.tracker.remove_expense(category, amount)
            messagebox.showinfo("Success", "Expense removed successfully!")
            self.remove_category_entry.delete(0, tk.END)
            self.remove_amount_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def view_expenses(self):
        expenses = self.tracker.get_expenses()
        expense_list = "\n".join([f"{category}: ${amount}" for category, amount in expenses.items()])
        total = f"\nTotal Expense: ${self.tracker.total_expense}"
        messagebox.showinfo("Expenses", expense_list + total)

    def view_category_percentages(self):
        percentages = self.tracker.category_percentages()
        percentage_list = "\n".join([f"{category}: {percent:.2f}%" for category, percent in percentages.items()])
        messagebox.showinfo("Category Percentages", percentage_list)

if __name__ == "__main__":
    root = tk.Tk()
    tracker = ExpenseTracker()
    gui = ExpenseTrackerGUI(root, tracker)
    root.mainloop()
