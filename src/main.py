# This entrypoint file to be used in development. Start by reading README.md
from pytest import main as pytest_main
from unittest import main as unittest_main
from budget_app.category import Category
from budget_app.create_spend_chart import create_spend_chart
from polygon_area_calculator.rectangle import Rectangle
from polygon_area_calculator.square import Square
from unittest import main

from arithmetic_arranger.arithmetic_arranger import arithmetic_arranger
from time_calculator.time_calculator import add_time
# arithmetic_arranger example code
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# time_calculator example code
print(add_time("11:06 PM", "2:02"))

# budget app example code
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

# Run unit tests automatically
pytest_main(['-vv'])
unittest_main(module='tests.test_time_calculator', exit=False)
unittest_main(module='tests.test_budget_app', exit=False)
unittest_main(module='tests.test_polygon_area_calculator', exit=False)
