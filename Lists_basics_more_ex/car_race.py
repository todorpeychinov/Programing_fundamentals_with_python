times_list = list(map(int, input().split()))
left_player_time = 0
right_player_time = 0

middle_of_the_list = len(times_list) // 2
left_part = times_list[:middle_of_the_list]
right_part = times_list[middle_of_the_list + 1:]
right_part = right_part[::-1]



for current_time in left_part:
    if current_time != 0:
        left_player_time += current_time
    else:
        left_player_time *= 0.8


for current_time in right_part:
    if current_time != 0:
        right_player_time += current_time
    else:
        right_player_time *= 0.8

if right_player_time < left_player_time:
    winner = 'right'
    winner_time = right_player_time
else:
    winner = 'left'
    winner_time = left_player_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")
