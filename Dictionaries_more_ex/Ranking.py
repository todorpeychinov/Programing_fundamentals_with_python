def check_contest(contest, contests_dict):
    if contest in contests_dict.keys():
        return True
    return False


def check_password(password, contest, contest_dict):
    if check_contest(contest, contest_dict):
        if contest_dict[contest] == password:
            return True
    return False


contests = {}
users = {}

while True:
    user_input = input()

    if user_input == 'end of contests':
        break

    contest, password = user_input.split(':')
    contests[contest] = password

while True:
    current_input = input()

    if current_input == 'end of submissions':
        break

    current_input_parts = current_input.split('=>')

    current_contest = current_input_parts[0]
    current_password = current_input_parts[1]
    current_username = current_input_parts[2]
    current_points = int(current_input_parts[3])

    if check_contest(current_contest, contests) and check_password(current_password, current_contest, contests):
        if current_username not in users:
            users[current_username] = [{'contest' : current_contest, 'points' : current_points}]
        else:
            for user_contest in users[current_username]:
                if user_contest['contest'] == current_contest:
                    if user_contest['points'] < current_points:
                        user_contest['points'] = current_points
                    break
            else:
                users[current_username].append({'contest' : current_contest, 'points' : current_points})

best_user = None
best_points = 0

for user, list_of_contest in users.items():
    current_user_total_points = 0
    for current_contest in list_of_contest:
        current_user_total_points += current_contest['points']

    if current_user_total_points > best_points:
        best_points = current_user_total_points
        best_user = user

print(f'Best candidate is {best_user} with total {best_points} points.')



# for user, list_of_contest in users.items():
#     print(user)
#     for current_contest in list_of_contest:
#         print(f"# {current_contest['contest']} -> {current_contest['points']}")
print("Ranking:")
for user in sorted(users.keys()):
    print(user)
    for current_contest in sorted(users[user], key=lambda x: x['points'], reverse=True):
        print(f"#  {current_contest['contest']} -> {current_contest['points']}")






