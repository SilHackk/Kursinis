import datetime

class Expense:
    def __init__(self, name, category, amount, user, date=None) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.user = user
        self.date = date if date else datetime.datetime.now()

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, {self.user} >"