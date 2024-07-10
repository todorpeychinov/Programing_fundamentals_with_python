number_of_dragons = int(input())
dragons = {}

for i in range(number_of_dragons):
    current_dragon = input().split()
    type = current_dragon[0]
    name = current_dragon[1]
    damage = current_dragon[2]
    health = current_dragon[3]
    armor = current_dragon[4]

    damage = int(damage) if damage != 'null' else 45
    health = int(health) if health != 'null' else 250
    armor = int(armor) if armor != 'null' else 10

    if type not in dragons:
        dragons[type] = []

    for dragon in dragons[type]:
        if dragon['name'] == name:
            dragon['damage'] = damage
            dragon['health'] = health
            dragon['armor'] = armor
            break
    else:
        dragons[type].append({'name': name, 'damage': damage, 'health': health, 'armor': armor})

for type, dragons_list in dragons.items():
    total_damage = sum(dragon['damage'] for dragon in dragons_list) / len(dragons_list)
    total_health = sum(dragon['health'] for dragon in dragons_list) / len(dragons_list)
    total_armor = sum(dragon['armor'] for dragon in dragons_list) / len(dragons_list)

    print(f"{type}::({total_damage:.2f}/{total_health:.2f}/{total_armor:.2f})")
    for dragon in sorted(dragons_list, key=lambda x: x['name']):
        print(f"-{dragon['name']} -> damage: {dragon['damage']}, health: {dragon['health']}, armor: {dragon['armor']}")

