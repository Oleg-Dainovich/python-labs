from functions import calculator_method, find_even_numbers

print("Hello, World!")

first_num = float(input())
second_num = float(input())
operation = input()
try:
    print(calculator_method (first_num, second_num, operation))
except ZeroDivisionError:
    print("Division by zero!")

find_even_numbers()
