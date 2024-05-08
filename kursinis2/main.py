import os
import calendar
import datetime

from models import Expense, User
from limits import LimitFactory, set_limits
from observer import Observer, UserLimitObserver

FILE_PATH = "expenses.csv"

if os.path.exists(FILE_PATH):
    os.remove(FILE_PATH)

def main():
    print(f"🎯 Running Finance Tracker!")
    expense_file_path = "expenses.csv"

    users = [
        User("User1", 100),
        User("User2", 100),
        # Add more users as needed
    ]
    observer = None

    if not os.path.exists(expense_file_path):
        observer = set_limits(users)

    while True:
        action = input("What would you like to do? (add/remove/set new limits/exit): ")
        
        if action.lower() == "set new limits":
            observer = set_limits(users)
        elif action.lower() == "add":
            for user in users:
                expense = get_user_expense(user)
                if expense:
                    save_expense_to_file(expense, expense_file_path)
                    summarize_expenses(expense_file_path, user, observer=observer)
                else:
                    print(red("Expense not saved due to limit exceeded."))
        elif action.lower() == "remove":
            if os.path.exists(expense_file_path) and os.path.getsize(expense_file_path) > 0:
                for user in users:
                    summarize_expenses(expense_file_path, user, remove=True)
            else:
                print("No expenses to remove.")
        elif action.lower() == "exit":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 'add', 'remove', 'set limits' or 'exit'.")

def get_user_expense(user):
    print(f"🎯 Getting User Expense for {user.name}")
    expense_name = input("Enter expense name: ")
    try:
        expense_amount = float(input("Enter expense amount: "))
    except ValueError:
        print(red("Invalid amount! Please enter a valid number."))
        return None
        
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
            selected_category = expense_categories[selected_index]
        except (ValueError, IndexError):
            print("Invalid category selection. Please try again!")
            continue

        new_expense = Expense(
            name=expense_name, 
            category=selected_category, 
            amount=expense_amount, 
            user=user
        )

        if any([
            new_expense.amount > user.daily_limit.limit_amount,
            new_expense.amount > user.weekly_limit.limit_amount,
            new_expense.amount > user.monthly_limit.limit_amount
        ]):
            print(red("You have exceeded your budget limit!"))
            return None

        return new_expense

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")  # Add this line for debugging
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category},{expense.user.name}\n")

def summarize_expenses(expense_file_path, user, remove=False, observer=None):
    print(f"🎯 Summarizing User Expense for {user.name}")
    expenses= []
    with open(expense_file_path,  encoding="utf-8") as f: 
        for line in f:
            expense_name, expense_amount, expense_category, expense_user = line.strip().split(",")
            if expense_user == user.name:
                line_expense = Expense(
                    name=expense_name,
                    amount=float(expense_amount),
                    category=expense_category,
                    user=user
                )
                expenses.append(line_expense)
        if not expenses:
            print("No expenses to remove.")
            return   
        
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = user.budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))

    print(f"Remaining Daily Budget: ${user.daily_limit.limit_amount - total_spent:.2f}")
    print(f"Remaining Weekly Budget: ${user.weekly_limit.limit_amount - total_spent:.2f}")
    print(f"Remaining Monthly Budget: ${user.monthly_limit.limit_amount - total_spent:.2f}")

    if observer:
        observer.notify("Expenses have been summarized.")

    if remove:
        expense_name_to_remove = input("Enter the name of the expense to remove: ").strip()
        expenses = [expense for expense in expenses if expense.name.strip() != expense_name_to_remove]
        if not expenses:
            print("No expenses matched your query.")
            return
        
        os.remove(expense_file_path)
        with open(expense_file_path, "a", encoding="utf-8") as f:
            for expense in expenses:
                f.write(f"{expense.name},{expense.amount},{expense.category},{expense.user.name}\n")
        print("Expense removed successfully!")

def green(text):
    return f"\033[92m{text}\033[0m"

def red(text):
    return f"\033[91m{text}\033[0m"

if __name__ == "__main__":
    main()