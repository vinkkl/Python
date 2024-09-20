class Expense:
    def __init__(self, expense_id, date, category, description, amount):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"ID: {self.expense_id}, Date: {self.date}, Category: {self.category}, Description: {self.description}, Amount: {self.amount}"


# Data Storage
expenses = []

# User Authentication
users = {
    "user1": "password1",
    "user2": "password2"
}


def authenticate_user(username, password):
    if username in users and users[username] == password:
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed!")
        return False


# Functions to manipulate the list
def add_expense(expense):
    expenses.append(expense)


def update_expense(expense_id, new_expense):
    for i, expense in enumerate(expenses):
        if expense.expense_id == expense_id:
            expenses[i] = new_expense
            return True
    return False


def delete_expense(expense_id):
    global expenses
    expenses = [expense for expense in expenses if expense.expense_id != expense_id]


def display_expenses():
    for expense in expenses:
        print(expense)


# Categorization and Summarization
def categorize_expenses():
    categories = {}
    for expense in expenses:
        if expense.category in categories:
            categories[expense.category] += expense.amount
        else:
            categories[expense.category] = expense.amount
    return categories


def summarize_expenses():
    total = 0
    for expense in expenses:
        total += expense.amount
    return total


# Functions for Repetitive Tasks
def calculate_total_expenses():
    return sum(expense.amount for expense in expenses)


def generate_summary_report():
    categories = categorize_expenses()
    print("Expense Summary by Category:")
    for category, amount in categories.items():
        print(f"{category}: {amount}")
    total = calculate_total_expenses()
    print(f"Total Expenses: {total}")


# Simple CLI for Interaction
def cli():
    while True:
        print("\nMenu:")
        print("1. Add a new expense")
        print("2. Update an existing expense")
        print("3. Delete an expense")
        print("4. Display all expenses")
        print("5. Generate a summary report")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            expense_id = int(input("Enter expense ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            expense = Expense(expense_id, date, category, description, amount)
            add_expense(expense)
        elif choice == '2':
            expense_id = int(input("Enter expense ID to update: "))
            date = input("Enter new date (YYYY-MM-DD): ")
            category = input("Enter new category: ")
            description = input("Enter new description: ")
            amount = float(input("Enter new amount: "))
            new_expense = Expense(expense_id, date, category, description, amount)
            if update_expense(expense_id, new_expense):
                print("Expense updated successfully.")
            else:
                print("Expense ID not found.")
        elif choice == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
            print("Expense deleted successfully.")
        elif choice == '4':
            print("\nExpenses:")
            display_expenses()
        elif choice == '5':
            print("\nSummary Report:")
            generate_summary_report()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")


# Example usage
if __name__ == "__main__":
   # username = input("Enter username: ")
   # password = input("Enter password: ")

    #if authenticate_user(username, password):
        cli()