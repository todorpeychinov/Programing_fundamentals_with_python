users_sides = {}

while True:
    user_input = input()

    if user_input == 'Lumpawaroo':
        break

    elif "|" in user_input:
        user_input = user_input.split(' | ')
        force_side = user_input[0]
        force_user = user_input[1]

        for current_list_of_users in users_sides.values():
            if force_user in current_list_of_users:
                break
        else:
            if force_side not in users_sides:
                users_sides[force_side] = []
            users_sides[force_side].append(force_user)

    elif "->" in user_input:
        user_input = user_input.split(' -> ')
        force_user = user_input[0]
        force_side = user_input[1]

        for current_list_of_users in users_sides.values():
            if force_user in current_list_of_users:
                current_list_of_users.remove(force_user)
        if force_side not in users_sides:
            users_sides[force_side] = []
        users_sides[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')

for side, users_list in users_sides.items():
    if users_list:
        print(f'Side: {side}, Members: {len(users_sides[side])}')
        for user in  users_list:
            print(f'! {user}')