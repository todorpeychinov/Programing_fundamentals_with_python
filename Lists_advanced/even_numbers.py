def even_numbers_indexes(list_of_integers):
    list_of_even_numbers_indexes = [index for index in range(len(list_of_integers)) if list_of_integers[index] % 2 == 0]
    return list_of_even_numbers_indexes

numbers_list = list(map(int, input().split(', ')))
print(even_numbers_indexes(numbers_list))