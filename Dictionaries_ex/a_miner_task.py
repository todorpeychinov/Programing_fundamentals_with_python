resources = {}

while True:
    material = input()

    if material == 'stop':
        break

    quantity = int(input())

    if material in resources.keys():
        resources[material] += quantity
    else:
        resources[material] = quantity

for current_material, current_quantity in resources.items():
    print(f'{current_material} -> {current_quantity}')
