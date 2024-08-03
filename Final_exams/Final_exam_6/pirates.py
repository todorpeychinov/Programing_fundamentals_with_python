def proser(cities, town, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    return cities


def plunder(cities, town, people, gold):
    cities[town]['population'] -= people
    cities[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
        del cities[town]
        print(f"{town} has been wiped off the map!")
    return cities


cities = {}

while True:
    command = input()

    if command == 'Sail':
        break

    city, population, gold = command.split('||')
    population = int(population)
    gold = int(gold)

    if city in cities:
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    else:
        cities[city] = {'population': population, 'gold': gold}

while True:
    event = input()

    if event == 'End':
        break

    event = event.split('=>')

    if event[0] == 'Plunder':
        town = event[1]
        people = int(event[2])
        gold = int(event[3])

        cities = plunder(cities, town, people, gold)

    elif event[0] == 'Prosper':
        town = event[1]
        gold = int(event[2])

        cities = proser(cities, town, gold)

if len(cities) > 0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for city in cities:
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")