def min_max_and_sum_of_numbers(list_of_numbers):
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    sum_of_numbers = sum(list_of_numbers)
    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_of_numbers}"

list_of_numbers = list(map(int, input().split()))
print(min_max_and_sum_of_numbers(list_of_numbers))