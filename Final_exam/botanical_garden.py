def water(plants_dict, sections_dict, plant_name, water_amount):
    if plant_name in plants_dict:
        plants_dict[plant_name]['water_needed'] -= water_amount
        if plants_dict[plant_name]['water_needed'] <= 0:
            current_plant_section = plants_dict[plant_name]['section']
            current_plant_count = plants_dict[plant_name]['count_of_plants']
            sections_dict[current_plant_section]['count_of_plants'] -= current_plant_count
            del plants_dict[plant_name]
            print(f"{plant_name} has been sufficiently watered.")

    return plants_dict, sections_dict



def plant(plants_dict, sections_dict, plant_name, water_needed, section):
    if plant_name not in plants_dict:
        plants_dict[plant_name] = {'water_needed': water_needed, 'section': section, 'count_of_plants': 1}
        if section not in sections_dict:
            sections_dict[section] = {'count_of_plants': 1}
        else:
            sections_dict[section]['count_of_plants'] += 1
    else:
        plants_dict[plant_name]['water_needed'] += water_needed
        plants_dict[plant_name]['count_of_plants'] += 1
        sections_dict[section]['count_of_plants'] += 1

    return plants_dict, sections_dict


plants_dict = {}
sections_dict = {}

while True:
    command = input()

    if command == 'EndDay':
        break

    command = command.split(': ')

    if command[0] == 'Plant':
        plant_name, water_needed, section = command[1].split('-')
        water_needed = int(water_needed)
        plants_dict, sections_dict = plant(plants_dict,sections_dict, plant_name, water_needed, section)

    elif command[0] == 'Water':
        plant_name, water_amount = command[1].split('-')
        water_amount = int(water_amount)
        plants_dict, sections_dict = water(plants_dict, sections_dict, plant_name, water_amount)


print("Plants needing water:")
for current_plant in plants_dict:
    print(f" {current_plant} -> {plants_dict[current_plant]['water_needed']}ml left")

print("Sections with thirsty plants:")
for current_section in sections_dict:
    if sections_dict[current_section]['count_of_plants'] > 0:
        print(f"{current_section}: {sections_dict[current_section]['count_of_plants']}")

