import unittest
from unittest.mock import patch
from io import StringIO
from main import User, set_limits, get_user_expense, save_expense_to_file, summarize_expenses, Expense

class TestFinanceFunctions(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.users = [
            User("User1", 100),
            User("User2", 100),
        ]
        self.expense_file_path = "test_expenses.csv"

    def test_set_limits(self):
        # Test set_limits function
        with patch("builtins.input", side_effect=["10", "10","10", "10", "50", "30", "200", "100"]):
            observer = set_limits(self.users)
        self.assertIsNotNone(observer)

    def test_get_user_expense(self):
        user = self.users[0]
        with patch("builtins.input", side_effect=["Test Expense", "20", "1"]):
            expense = get_user_expense(user)
        self.assertIsNotNone(expense)

    def test_save_expense_to_file(self):
        # Test save_expense_to_file function
        user = self.users[0]
        # Selecting the category index corresponding to "🍔 Food"
        user.expenses.append(Expense("Test Expense", 50, 1, user))
        expense = user.expenses[0]
        save_expense_to_file(expense, self.expense_file_path)
        # Check if file is created and contains data
        with open(self.expense_file_path, "r") as f:
            data = f.read()
        self.assertTrue(len(data) > 0)

    def test_summarize_expenses(self):
        # Test summarize_expenses function
        user = self.users[0]
        # Create a mock expense file
        with open(self.expense_file_path, "w") as f:
            f.write("Test Expense,20,Food,User1\n")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            summarize_expenses(self.expense_file_path, user)
            output = fake_out.getvalue().strip()
        self.assertTrue("Total Spent" in output)



if __name__ == "__main__":
    unittest.main()
