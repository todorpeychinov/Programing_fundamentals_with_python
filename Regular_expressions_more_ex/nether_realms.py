import re

demons_names = input().split(', ')
demons_names = sorted(demons_names)
demons_book = {}

pattern_characters = r'[^0-9\+\-\*\/\.]'
pattern_numbers = r'[+-]?[0-9]+\.?[0-9]*'
pattern_signs = r'[\*\/]'


for demon in demons_names:
    health = 0
    damage = 0

    characters = re.findall(pattern_characters, demon)
    numbers = re.finditer(pattern_numbers, demon)
    numbers_list = []

    for number in numbers:
        numbers_list.append(float(number.group()))

    signs = re.findall(pattern_signs, demon)

    for character in characters:
        health += ord(character)

    for number in numbers_list:
        damage += number

    for sign in signs:
        if sign == '*':
            damage *= 2
        elif sign == '/':
            damage /= 2

    demons_book[demon] = {'Health': health, 'Damage': damage}

for demon in demons_book:
    print(f"{demon} - {demons_book[demon]['Health']} health, {demons_book[demon]['Damage']:.2f} damage")




