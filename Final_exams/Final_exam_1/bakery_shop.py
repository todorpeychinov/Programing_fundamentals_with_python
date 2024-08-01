stock = {}
all_sold = 0

while True:
    command = input()

    if command == 'Complete':
        break

    command = command.split()

    if command[0] == 'Receive':
        quantity = int(command[1])
        food = command[2]

        if quantity > 0:
            if food not in stock:
                stock[food] = quantity
            else:
                stock[food] += quantity

    elif command[0] == 'Sell':
        quantity = int(command[1])
        food = command[2]

        if food not in stock:
            print(f'You do not have any {food}.')
        elif stock[food] < quantity:
            print(f"There aren't enough {food}. You sold the last {stock[food]} of them.")
            all_sold += stock[food]
            del stock[food]
        else:
            all_sold += quantity
            stock[food] -= quantity
            print(f'You sold {quantity} {food}.')
            if stock[food] == 0:
                del stock[food]


for current_food in stock:
    print(f'{current_food}: {stock[current_food]}')

print(f"All sold: {all_sold} goods")