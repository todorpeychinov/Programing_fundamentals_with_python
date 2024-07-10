contests = {}
users_statistics = {}

already_exists = False


while True:
    command = input().split(" -> ")

    if command[0] == 'no more time':
        break


    current_username = command[0]
    current_contest = command[1]
    current_points = int(command[2])

    if current_contest not in contests.keys():
        contests[current_contest] = [{'username': current_username, 'points': current_points}]
    else:
        user_already_exists = False
        for contest, list_of_users in contests.items():
            for current_user in list_of_users:
                if current_user['username'] == current_username and contest == current_contest:
                    user_already_exists = True
                    if current_user['points'] < current_points:
                        current_user['points'] = current_points
                    break
        if not user_already_exists:
            contests[current_contest].append({'username': current_username, 'points': current_points})

for current_contest, current_contest_users in contests.items():
    print(f"{current_contest}: {len(current_contest_users)} participants")
    sorted_dict = sorted(current_contest_users, key=lambda x: (-x["points"], x["username"]))
    counter = 0
    for user in sorted_dict:
        counter += 1
        print(f"{counter}. {user['username']} <::> {user['points']}")

for current_contest, current_contest_users in contests.items():
    for user in current_contest_users:
        if user['username'] not in users_statistics.keys():
           users_statistics[user['username']] = user['points']
        else:
            users_statistics[user['username']] += user['points']

print("Individual standings:")
sorted_statistics = dict(sorted(users_statistics.items(), key=lambda item: (-item[1], item[0])))

counter = 0
for user, points in sorted_statistics.items():
    counter += 1
    print(f'{counter}. {user} -> {points}')




