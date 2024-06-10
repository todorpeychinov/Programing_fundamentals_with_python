number_of_integer = int(input())
integers_list = []
filtered_list = []

for number in range(number_of_integer):
    current_number = int(input())
    integers_list.append(current_number)

command = input()

if command == "even":
    for number in integers_list:
        if number % 2 == 0:
            filtered_list.append(number)
elif command == "odd":
    for number in integers_list:
        if number % 2 != 0:
            filtered_list.append(number)
elif command == "negative":
    for number in integers_list:
        if number < 0:
            filtered_list.append(number)
elif command == "positive":
    for number in integers_list:
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)