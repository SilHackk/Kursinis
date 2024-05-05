from abc import ABC, abstractmethod
from observer import Observer, UserLimitObserver

class Limit(ABC):
    def __init__(self, limit_amount) -> None:
        self.limit_amount = limit_amount

    @abstractmethod
    def get_limit(self):
        pass

class DailyLimit(Limit):
    def get_limit(self):
        return f"Daily limit: {self.limit_amount}"

class WeeklyLimit(Limit):
    def get_limit(self):
        return f"Weekly limit: {self.limit_amount}"

class MonthlyLimit(Limit):
    def get_limit(self):
        return f"Monthly limit: {self.limit_amount}"

class LimitFactory:
    @staticmethod
    def create_limit(limit_type, limit_amount):
        if limit_type.lower() == "daily":
            return DailyLimit(limit_amount)
        elif limit_type.lower() == "weekly":
            return WeeklyLimit(limit_amount)
        elif limit_type.lower() == "monthly":
            return MonthlyLimit(limit_amount)
        else:
            raise ValueError("Invalid limit type")

def set_limits(users):
    print("Enter new deposit limits:")
    observer = Observer()
    limit_factory = LimitFactory()
    for user in users:
        while True:
            try:
                user.budget = float(input(f"Budget for {user.name}: "))
                daily_limit_amount = float(input(f"Daily limit for {user.name}: "))
                weekly_limit_amount = float(input(f"Weekly limit for {user.name}: "))
                monthly_limit_amount = float(input(f"Monthly limit for {user.name}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        user.daily_limit = limit_factory.create_limit("daily", daily_limit_amount)
        user.weekly_limit = limit_factory.create_limit("weekly", weekly_limit_amount)
        user.monthly_limit = limit_factory.create_limit("monthly", monthly_limit_amount)
        
        user_observer = UserLimitObserver(user)
        observer.register(user_observer)

    print("Limits updated successfully!")
    return observer
