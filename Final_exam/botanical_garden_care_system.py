def plant(plants_dict, plant_name, water_needed, section):
    if plant_name not in plants_dict:
        plants_dict[plant_name] = {'water_needed': water_needed, 'section': section, 'section_counter': 1}
    else:
        plants_dict[plant_name]['water_needed'] += water_needed
        plants_dict[plant_name]['section_counter'] += 1

    return plants_dict


def water(plants_dict, plant_name, water_amount):
    if plant_name in plants_dict:
        plants_dict[plant_name]['water_needed'] -= water_amount
        if plants_dict[plant_name]['water_needed'] <= 0:
            del plants_dict[plant_name]
            print(f"{plant_name} has been sufficiently watered.")

    return plants_dict


plants_dict = {}

while True:
    command = input()

    if command == 'EndDay':
        break

    command = command.split(': ')

    if command[0] == 'Plant':
        plant_name, water_needed, section = command[1].split('-')
        water_needed = int(water_needed)
        plants_dict = plant(plants_dict, plant_name, water_needed, section)

    elif command[0] == 'Water':
        plant_name, water_amount = command[1].split('-')
        water_amount = int(water_amount)
        plants_dict = water(plants_dict, plant_name, water_amount)

print("Plants needing water:")
for current_plant in plants_dict:
    print(f" {current_plant} -> {plants_dict[current_plant]['water_needed']}ml left")

print("Sections with thirsty plants:")
for current_plant in plants_dict:
    print(f" {plants_dict[current_plant]['section']}: {plants_dict[current_plant]['section_counter']}")


