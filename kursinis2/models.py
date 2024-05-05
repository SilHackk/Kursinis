import datetime
from limits import LimitFactory

class Expense:
    def __init__(self, name, category, amount, user, date=None):
        self.name = name
        self.category = category
        self.amount = float(amount)  # Convert amount to float
        self.user = user
        self.date = date if date else datetime.datetime.now()

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, {self.user} >"
    
class User:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.daily_limit = LimitFactory.create_limit("daily", budget)
        self.weekly_limit = LimitFactory.create_limit("weekly", budget)
        self.monthly_limit = LimitFactory.create_limit("monthly", budget)
        self.expenses = []

    def __str__(self):
        return f"User(name={self.name}, budget={self.budget})"