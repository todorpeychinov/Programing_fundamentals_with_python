players_pool = {}

while True:
    command = input()

    if command == 'Season end':
        break

    elif '->' in command:
        command = command.split(' -> ')
        player, position = command[0], command[1]
        skills = int(command[2])

        if player not in players_pool:
            players_pool[player] = [{'position': position, 'skills': skills}]

        else:

            for current_player in players_pool[player]:
                if current_player['position'] == position:
                    if current_player['skills'] < skills:
                        current_player['skills'] = skills
                    break
            else:
                players_pool[player].append({'position': position,'skills': skills})

    else:
        command = command.split(' vs ')
        player_one = command[0]
        player_two = command[1]
        have_similar_positions = False

        if player_one in players_pool and player_two in players_pool:
            player_one_positions = []
            player_one_points = 0
            player_two_positions = []
            player_two_points = 0

            for player_one_position in players_pool[player_one]:
                player_one_positions.append(player_one_position['position'])
                player_one_points += player_one_position['skills']

            for player_two_position in players_pool[player_two]:
                player_two_positions.append(player_two_position['position'])
                player_two_points += player_two_position['skills']

            for current_position in player_one_positions:
                if current_position in player_two_positions:
                    have_similar_positions = True
                    break

            if have_similar_positions:
                if player_one_points > player_two_points:
                    del players_pool[player_two]
                elif player_two_points > player_one_points:
                    del players_pool[player_one]


players_total_points = {}

for player, list_of_positions in players_pool.items():
    players_total_points[player] = {'points': 0}
    for position in list_of_positions:
        players_total_points[player]['points'] += position['skills']

sorted_players = dict(sorted(players_total_points.items(), key=lambda x: (-x[1]['points'], x[0])))

for player in sorted_players:
    print(f"{player}: {sorted_players[player]['points']} skill")
    sorted_player_skills = sorted(players_pool[player], key=lambda x: (-x['skills'], x['position']))
    for current_position in sorted_player_skills:
        print(f"- {current_position['position']} <::> {current_position['skills']}")



