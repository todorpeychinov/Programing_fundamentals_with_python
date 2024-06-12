def even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False

def filtered_numbers(list_of_numbers):
    list_of_even_numbers = filter(even_number, list_of_numbers)
    return list(list_of_even_numbers)

list_of_numbers = list(map(int,input().split()))

print(filtered_numbers(list_of_numbers))
