import tkinter as tk
from tkinter import messagebox

# Initial expenses
expenses = [
    {'amount': '51.00', 'category': 'shirt'},
    {'amount': '21.55', 'category': 'groceries'},
    {'amount': '52.00', 'category': 'headphone'}
]

def listExpenses():
    """Displays the list of expenses in the UI."""
    expenses_listbox.delete(0, tk.END)  # Clear current list
    for idx, expense in enumerate(expenses):
        expenses_listbox.insert(tk.END, f"#{idx} - {expense['amount']} - {expense['category']}")

def addExpense():
    """Adds a new expense based on user input."""
    amount = amount_entry.get()
    category = category_entry.get()
    
    if amount and category:
        expenses.append({'amount': amount, 'category': category})
        listExpenses()  # Update the list
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Input Error", "Please enter both amount and category.")

def removeExpense():
    """Removes an expense based on the selected index in the listbox."""
    try:
        selected_idx = expenses_listbox.curselection()[0]
        del expenses[selected_idx]
        listExpenses()  # Update the list
    except IndexError:
        messagebox.showerror("Selection Error", "Please select an expense to remove.")

# Set up the main window
root = tk.Tk()
root.title("Expense Manager")

# Create the UI components
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=1, column=0, padx=10, pady=10)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Expense", command=addExpense)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

expenses_listbox = tk.Listbox(root, width=40, height=10)
expenses_listbox.grid(row=3, column=0, columnspan=2, pady=10)

remove_button = tk.Button(root, text="Remove Selected Expense", command=removeExpense)
remove_button.grid(row=4, column=0, columnspan=2, pady=10)

# Initial listing of expenses
listExpenses()

# Run the main event loop
root.mainloop()
