import re

pattern = r'@([A-Za-z]+)[^@:!\->]*:(\d+)[^@:!\->]*!([A|D])![^@:!\->]*\->(\d+)'
letters = ['s', 't', 'a', 'r', 'S', 'T', 'A', 'R']

attacked_planets = []
destroyed_planets = []

number_of_messages = int(input())

for _ in range(number_of_messages):
    letters_counter = 0
    new_message = ''
    current_message = input()

    for character in letters:
        letters_counter += current_message.count(character)

    for current in current_message:
        new_message += chr(ord(current) - letters_counter)

    match = re.search(pattern, new_message)

    if match:
        planet = match.group(1)
        attack_type = match.group(3)

        if attack_type == 'A':
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

sorted_attacked_planets = sorted(attacked_planets)
sorted_destroyed_planets = sorted(destroyed_planets)

print(f'Attacked planets: {len(attacked_planets)}')
for attacked_planet in sorted_attacked_planets:
    print(f'-> {attacked_planet}')

print(f'Destroyed planets: {len(destroyed_planets)}')
for destroyed_planet in sorted_destroyed_planets:
    print(f'-> {destroyed_planet}')
