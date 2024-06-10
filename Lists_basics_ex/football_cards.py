team_a = []
team_b = []
game_was_terminatred = False

for i in range(1, 12):
    team_a.append('A-' + str(i))
    team_b.append('B-' + str(i))

cards = input().split()

for card in cards:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminatred = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminatred:
    print("Game was terminated")


