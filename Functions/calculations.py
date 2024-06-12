def calculate(operator_as_string, first_number, second_number):
    if operator_as_string == 'multiply':
        result = first_number * second_number
    elif operator_as_string == 'divide':
        result = first_number / second_number
    elif operator_as_string == 'add':
        result = first_number + second_number
    elif operator_as_string == 'subtract':
        result = first_number - second_number
    return int(result)


operator_as_string = input()
first_number = int(input())
second_number = int(input())
print(calculate(operator_as_string, first_number, second_number))