import csv
import os
from datetime import datetime

EXPENSES_FILE = "expenses.csv"

def init_file():
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount", "Category"])

def add_expense():
    amount = float(input("Enter amount spent: $"))
    category = input("Enter category (e.g., Food, Transport): ").capitalize()
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(EXPENSES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category])
    print(f"✅ Added ${amount:.2f} under '{category}'")

def view_expenses():
    try:
        with open(EXPENSES_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader) 
            expenses = list(reader)
            
            if not expenses:
                print("No expenses recorded yet!")
                return
                
            print("\n📝 All Expenses:")
            total = 0
            for i, (date, amount, category) in enumerate(expenses, 1):
                print(f"{i}. {date} | ${float(amount):.2f} | {category}")
                total += float(amount)
            print(f"\n💵 Total: ${total:.2f}")
            
    except FileNotFoundError:
        print("No expenses recorded yet!")

def show_analytics():
    try:
        with open(EXPENSES_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)
            expenses = list(reader)
            
            if not expenses:
                print("No data for analytics!")
                return
                
            total = sum(float(expense[1]) for expense in expenses)
            
            categories = {}
            for _, amount, category in expenses:
                categories[category] = categories.get(category, 0) + float(amount)
            
            print("\n📊 Analytics")
            print(f"Total Spending: ${total:.2f}")
            print("\nBy Category:")
            for category, amount in categories.items():
                print(f"- {category}: ${amount:.2f} ({(amount/total)*100:.1f}%)")
                
    except FileNotFoundError:
        print("No expenses recorded yet!")

def main():
    init_file()
    while True:
        print("\n💸 Expense Tracker CLI")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Analytics")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_analytics()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()