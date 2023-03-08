from functions import *

print("Hello, World!")

first_num = float(input())
second_num = float(input())
operation = input()
try:
    print(calculator_method (first_num, second_num, operation))
except ZeroDivisionError:
    print("Division by zero!")

print(find_even_numbers())
