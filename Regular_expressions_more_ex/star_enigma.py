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




'''
import re

letters = ['s', 't', 'a', 'r', 'S', 'T', 'A', 'R']
planet_pattern = r'@([A-Za-z]+)'
population_pattern = r':(\d+)'
attack_pattern = r'!([AD])!'
soldier_pattern = r'->(\d+)'

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

    planet = re.search(planet_pattern, new_message)
    population = re.search(population_pattern, new_message)
    attack_type = re.search(attack_pattern, new_message)
    soldiers = re.search(soldier_pattern, new_message)

    if planet and population and attack_type and soldiers:
        planet = planet.group(1)
        population = int(population.group(1))
        attack_type = attack_type.group(1)
        soldiers = int(soldiers.group(1))

        if attack_type == 'A':
            attacked_planets.append(planet)
        elif attack_type == 'D':
            destroyed_planets.append(planet)


sorted_attacked_planets = sorted(attacked_planets)
sorted_destroyed_planets = sorted(destroyed_planets)

print(f'Attacked planets: {len(attacked_planets)}')
for attacked_planet in sorted_attacked_planets:
    print(f'-> {attacked_planet}')

print(f'Destroyed planets: {len(destroyed_planets)}')
for destroyed_planet in sorted_destroyed_planets:
    print(f'-> {destroyed_planet}')

'''














