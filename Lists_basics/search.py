number_of_strings = int(input())
keyword = input()
all_strings = []
filtered_strings = []

for string in range(number_of_strings):
    current_string = input()
    all_strings.append(current_string)

for current_string in all_strings:
    if keyword in current_string:
        filtered_strings.append(current_string)

print(all_strings)
print(filtered_strings)

