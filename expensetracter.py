# expense_tracker.py

expenses = []

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Shopping): ")
    amount = float(input("Enter the amount: "))
    
    expense = {"date": date, "category": category, "amount": amount}
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    
    print("\n📊 Your Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} - {expense['category']} - ${expense['amount']:.2f}")
    print()

def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\n💰 Total Expenses: ${total:.2f}\n")

def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
