def rounding_numbers(list_of_numbers):
    list_of_rounded_numbers = []
    for number in list_of_numbers:
        list_of_rounded_numbers.append(round(number))
    return list_of_rounded_numbers

list_of_numbers = list(map(float, input().split()))
print(rounding_numbers(list_of_numbers))