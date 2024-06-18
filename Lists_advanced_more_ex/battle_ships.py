def process_attacks(attacks, ship_map):
    destroyed_ships = 0
    for attack in attacks:
        attack_list = attack.split('-')
        row = int(attack_list[0])
        col = int(attack_list[1])
        if ship_map[row][col] != 0:
            ship_map[row][col] -= 1
            if ship_map[row][col] == 0:
                destroyed_ships += 1
    return destroyed_ships

number_of_rows = int(input())

ship_map = []

for row in range(number_of_rows):
    current_row = list(map(int,input().split()))
    ship_map.append(current_row)

attack_list = input().split()

result = process_attacks(attack_list, ship_map)
print(result)
