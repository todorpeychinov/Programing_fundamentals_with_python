first_character = input()
second_character = input()
some_string = input()

minimal_ascii_number = ord(first_character)
maximal_ascii_number = ord(second_character)
total_sum = 0

for character in some_string:
    if minimal_ascii_number < ord(character) < maximal_ascii_number:
        total_sum += ord(character)

print(total_sum)