number_of_cars = int(input())

cars = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {'mileage': mileage, 'fuel': fuel}

while True:
    command = input()

    if command == 'Stop':
        break

    command = command.split(' : ')

    if command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel_consumed = int(command[3])

        if cars[car]['fuel'] < fuel_consumed:
            print('Not enough fuel to make that ride')
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel_consumed
            print(f'{car} driven for {distance} kilometers. {fuel_consumed} liters of fuel consumed.')

        if cars[car]['mileage'] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")

    elif command[0] == 'Refuel':
        car = command[1]
        fuel_to_add = int(command[2])
        if cars[car]['fuel'] + fuel_to_add > 75:
            added_fuel = 75 - cars[car]['fuel']
            cars[car]['fuel'] = 75
            print(f"{car} refueled with {added_fuel} liters.")
        else:
            cars[car]['fuel'] += fuel_to_add
            print(f"{car} refueled with {fuel_to_add} liters.")

    elif command[0] == 'Revert':
        car = command[1]
        kilometers_to_revert = int(command[2])
        cars[car]['mileage'] -= kilometers_to_revert
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers_to_revert} kilometers")

for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")
