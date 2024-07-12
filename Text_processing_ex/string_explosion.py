some_string = input()
strength = 0
strength_number = ''
final_string = ''

for index in range(len(some_string)):
    if some_string[index] != '>' and strength > 0:
        strength -= 1

    elif some_string[index] == '>':
        final_string += some_string[index]
        for digit in range(index + 1, len(some_string)):
            if not some_string[digit].isdigit():
                break
            strength_number += some_string[digit]
        strength += int(strength_number)
        strength_number = ''

    else:
        final_string += some_string[index]

print(final_string)