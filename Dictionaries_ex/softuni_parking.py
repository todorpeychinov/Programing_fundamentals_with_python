parking = {}
n = int(input())

for i in range(n):
    user_input = input().split()

    if user_input[0] == 'register':
        username = user_input[1]
        license_plate = user_input[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif user_input[0] == 'unregister':
        username = user_input[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for user, plate in parking.items():
    print(f"{user} => {plate}")


