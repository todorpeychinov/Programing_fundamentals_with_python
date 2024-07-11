input_string = input()

letters = ''
numbers = ''
others = ''

for character in input_string:
    if character.isalpha():
        letters += character
    elif character.isdigit():
        numbers += character
    else:
        others += character

print(numbers)
print(letters)
print(others)

