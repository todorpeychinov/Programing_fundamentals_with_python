some_string = input()
last_character = ''
final_string = ''

for character in some_string:
    if character != last_character:
        final_string += character
        last_character = character

print(final_string)
