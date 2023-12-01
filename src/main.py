# This entrypoint file to be used in development. Start by reading README.md
from pytest import main as pytest_main
from unittest import main as unittest_main

from arithmetic_arranger.arithmetic_arranger import arithmetic_arranger
from time_calculator.time_calculator import add_time
# arithmetic_arranger example code
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# time_calculator example code
print(add_time("11:06 PM", "2:02"))

# Run unit tests automatically
pytest_main(['-vv'])
unittest_main(module='tests.test_time_calculator', exit=False)