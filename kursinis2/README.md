---
# Introduction :wink:

The goal of this coursework is to develop a finance tracking application that enables users to track their expenses, set deposit limits on a daily, weekly, and monthly basis, and manage expense history efficiently. The application is designed to help users manage their finances more effectively by providing insights into their spending habits and ensuring they stay within their budget limits.

## **What is the Application?**

- Track their expenses by entering details such as expense name, amount, and category.
- Set deposit limits on a daily, weekly, and monthly basis to manage their budget effectively.
- Add and remove expenses as needed.
- Print expense history to review past transactions.
- Save expense history to a file for record-keeping purposes.

## **How to Run the Program:**

1. Ensure you have Python installed on your system.
2. Download the provided source code files.
3. Make sure you have the necessary dependencies installed, including the `models.py`, `limits.py`, and `observer.py` files.
4. Run the `finance_tracker.py` file using a Python interpreter.

## **How to Use the Program:**

Once the program is running, follow these steps to utilize its features:

1. Upon starting the program, you will be prompted with options such as adding expenses, removing expenses, setting new limits, or exiting the program.
2. To add an expense, choose the "add" option and enter the required details such as expense name, amount, and category. The program will check if the expense exceeds the user's set limits before saving it.
3. To remove an expense, select the "remove" option and follow the prompts to remove a specific expense from the history.
4. To set new deposit limits, select the "set new limits" option and input the desired budget and deposit limits for each user.
5. To exit the program, choose the "exit" option.

The program provides real-time summaries of expenses, remaining budgets, and notifications if budget limits are exceeded. Additionally, it offers the functionality to save and print expense history for future reference and it can handle group deposits for multiple users.

---
# Body/Analysis :yum:

The program implement all 4 object-oriented programming pillars:

+ [Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
+ [Abstraction](https://en.wikipedia.org/wiki/Abstraction)
+ [Inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
+ [Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))

***
## 1. **Polymorphism:**
Describes situations in which something occurs in several different forms.

+ Polymorphism is best demonstrated in the LimitFactory class, where different types of limits are created based on the user's input. Each limit object behaves differently based on its specific type.

```
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
```
+ The `Expense` class demonstrates polymorphism as well. While each expense object shares common attributes such as name, amount, and category, they can represent various types of expenses, such as food, housing, or entertainment.
```
class Expense:
    def __init__(self, name, category, amount, user, date=None):
        # Constructor implementation
    
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, {self.user} >"
```
***
## 2. **Abstraction:**
The ability to hide complex implementation details and show only the necessary features of an object. 

+ Abstraction is achieved through classes and methods that encapsulate functionality and expose only essential features to the user. For example, users interact with the program through a simple command-line interface without needing to understand the internal workings.
```
class Limit(ABC):
    @abstractmethod
    def get_limit(self):
        pass
```
+ The Observer class provides an abstract interface for implementing observers without exposing the internal implementation details.
```
class Observer:
    def __init__(self) -> None:
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)
```
***
## 3. **Inheritance:**
A mechanism that allows a class to inherit properties and behaviors from another class.

+ Inheritance is exemplified in subclasses like DailyLimit, WeeklyLimit, and MonthlyLimit, which inherit from the Limit class and provide specialized behavior while reusing common functionality.
```
class DailyLimit(Limit):
    def get_limit(self):
        return f"Daily limit: {self.limit_amount}"
```
+ The User class inherits properties and methods from the Observer class to facilitate observing changes in user limits.
```
class User(Observer):
```
***
## 4. **Encapsulation:**
A way to restrict the direct access to some components of an object, so users cannot access state values for all of the variables of a particular object.

+ Encapsulation is evident in classes like Expense, User, Limit, and Observer, where attributes and methods related to each entity are encapsulated within their respective classes.
```
class Expense:
    def __init__(self, name, category, amount, user, date=None):
        # Constructor implementation
    
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, {self.user} >"
```
+ Access to internal data and methods is controlled through access modifiers like public, private, and protected. For instance, the amount attribute of the Expense class is encapsulated and accessed through public methods like get_amount() and set_amount(), ensuring data integrity and security.
***
# Results and Summary 😊

## Results:

+ Implementing the finance tracking application successfully demonstrated the practical application of object-oriented programming principles.
+ It was a bit of a challenge at first to understand how unittest works and correct errors.
+ Another challenge was choosing which design pattern would fit the best.
+ Despite these challenges, the program effectively tracked expenses, allowed users to set limits, and provided insights into their financial habits.

## Conclusions:
This coursework has achieved a functional finance tracking program that empowers users to manage their expenses and budgets effectively. The program's contains all 4 OOP principles and 2 design paterns. 
In the future, I plan to add a savings feature so users can keep track of how much they're saving along with their expenses, helping them manage their money better. It would also be great to connect the app with online banking, so users can see their spending in real-time. And maybe down the line, we could add smart features that use AI to give personalized money advice, making the app even more helpful. Overall, I think this is a great start!
***
