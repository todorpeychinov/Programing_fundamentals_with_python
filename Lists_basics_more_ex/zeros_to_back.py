user_input = input().split(',')
numbers_list = []


for number in user_input:
    numbers_list.append(int(number))


for current_number in numbers_list:
    if current_number == 0:
        numbers_list.remove(current_number)
        numbers_list.append(current_number)

print(numbers_list)
