
list_of_integer = input().split()

count_of_numbers_to_remove = int(input())

# for numbers in range(count_of_numbers_to_remove):
#     min_number = 99999999999999999999999999999
#     for number in list_of_integer:
#         if int(number) < min_number:
#             min_number = int(number)
#     list_of_integer.remove(str(min_number))
#
#

for numbers in range(count_of_numbers_to_remove):
    list_of_integer.remove(min(list_of_integer))


print(", ".join(list_of_integer))

