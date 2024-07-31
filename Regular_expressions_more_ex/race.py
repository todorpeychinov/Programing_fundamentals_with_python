import re

list_of_participants = input().split(', ')

race_dict = {}

pattern_numbers = r'\d'
pattern_letters = r'[A-Za-z]'

while True:
    info = input()

    if info == 'end of race':
        break

    match_numbers = re.findall(pattern_numbers, info)
    match_letters = re.findall(pattern_letters, info)

    name = "".join(match_letters)
    current_points = 0

    for current_number in match_numbers:
        current_number = int(current_number)
        current_points += current_number

    if name in list_of_participants:
        if name in race_dict:
            race_dict[name] += current_points
        else:
            race_dict[name] = current_points

sorted_race_dict = sorted(race_dict.items(), key=lambda x: x[1], reverse=True)

print(f'1st place: {sorted_race_dict[0][0]}')
print(f'2nd place: {sorted_race_dict[1][0]}')
print(f'3rd place: {sorted_race_dict[2][0]}')