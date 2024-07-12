some_string = input()
final_string = ''
sub_string = ''
number = ''

for index in range(len(some_string)):
    if not some_string[index].isdigit():
        sub_string += some_string[index].upper()
    else:
        for current_number_index in range(index, len(some_string)):
            if some_string[current_number_index].isdigit():
                number += some_string[current_number_index]
            else:
                break
        final_string += sub_string * int(number)
        number = ''
        sub_string = ''


print(f'Unique symbols used: {len(set(final_string))}')
print(final_string)
