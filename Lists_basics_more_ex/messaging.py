numbers_list = input().split()
current_string = list(input())
number_of_indexes = len(current_string)
message = ''


for current_number in numbers_list:
    current_index = 0
    for digit in current_number:
        current_index += int(digit)

    while current_index > number_of_indexes - 1:
        current_index -= number_of_indexes

    message += current_string[current_index]
    current_string.pop(current_index)
    number_of_indexes -= 1

print(message)




