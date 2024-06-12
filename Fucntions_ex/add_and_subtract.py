def sum_numbers(first_integer, second_integer):
    return first_integer + second_integer

def subtract(sum_of_ints, third_integer):
    return sum_of_ints - third_integer

def add_and_subtract(first_integer, second_integer, third_integer):
    return subtract(sum_numbers(first_integer, second_integer), third_integer)

first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

print(add_and_subtract(first_integer, second_integer, third_integer))