# This entrypoint file to be used in development. Start by reading README.md
from pytest import main as pytest_main
from unittest import main as unittest_main
import budget_app.category as category
from budget_app.create_spend_chart import create_spend_chart

from arithmetic_arranger.arithmetic_arranger import arithmetic_arranger
from time_calculator.time_calculator import add_time
# arithmetic_arranger example code
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# time_calculator example code
print(add_time("11:06 PM", "2:02"))

# budget app example code
food = category.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = category.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = category.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
pytest_main(['-vv'])
unittest_main(module='tests.test_time_calculator', exit=False)
unittest_main(module='tests.test_budget_app', exit=False)
