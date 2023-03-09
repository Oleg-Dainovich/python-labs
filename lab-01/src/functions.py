def calculator_method (first_number, second_number, operation):
    if (operation == "add"):
        return first_number + second_number
    elif (operation == "sub"):
        return first_number - second_number
    elif (operation == "mult"):
        return first_number * second_number
    elif (operation == "div"):
        return first_number / second_number

def find_even_numbers ():
    numbers_list = [int(index) for index in input().split()]
    for number in numbers_list:
        if (number % 2 == 1):
            numbers_list.remove(number)

    return numbers_list
