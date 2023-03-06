from functions import *

print("Hello, World!")

first_num = input()
second_num = input()
operation = input()
try:
    calculator_method (first_num, second_num, operation)
except ZeroDivisionError:
    print("Division by zero!")

find_even_numbers()
