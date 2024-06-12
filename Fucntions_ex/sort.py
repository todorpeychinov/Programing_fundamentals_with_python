def sort_function(list_of_numbers):
    sorted_list_of_numbers = sorted(list_of_numbers)
    return sorted_list_of_numbers


list_of_numbers = list(map(int, input().split()))
print(sort_function(list_of_numbers))
