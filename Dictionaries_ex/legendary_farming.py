materials = {"shards": 0, "fragments": 0, "motes": 0}
item_won = None

while True:
    list_of_items = input().split()
    for index in range(0, len(list_of_items), 2):
        current_quantity = int(list_of_items[index])
        current_item = (list_of_items[index + 1]).lower()

        if current_item in materials.keys():
            materials[current_item] += current_quantity
        else:
            materials[current_item] = current_quantity

        if materials['shards'] >= 250:
            materials['shards'] -= 250
            item_won = 'Shadowmourne'
            break

        elif materials['fragments'] >= 250:
            materials['fragments'] -= 250
            item_won = 'Valanyr'
            break

        elif materials['motes'] >= 250:
            materials['motes'] -= 250
            item_won = 'Dragonwrath'
            break
    if item_won:
        break

print(f"{item_won} obtained!")
for material, quantity in materials.items():
    print(f'{material}: {quantity}')


