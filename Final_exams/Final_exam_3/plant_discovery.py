number_of_inputs = int(input())

plants = {}

for _ in range(number_of_inputs):
    plant_name, rarity = input().split('<->')
    plants[plant_name] = {'rarity': int(rarity), 'rating': 0, 'rating_count': 0}

while True:
    command = input()
    if command == 'Exhibition':
        break

    command = command.split(': ')


    if command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        if plant in plants:
            plants[plant]['rating'] += float(rating)
            plants[plant]['rating_count'] += 1
        else:
            print('error')

    elif command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        new_rarity = int(new_rarity)
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print('error')

    elif command[0] == 'Reset':
        plant = command[1]
        if plant in plants:
            plants[plant]['rating'] = 0
            plants[plant]['rating_count'] = 0
        else:
            print('error')

print('Plants for the exhibition:')

for plant in plants:
    average_rating = plants[plant]['rating'] / plants[plant]['rating_count'] if plants[plant]['rating_count'] > 0 else 0
    print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {average_rating:.2f}")
