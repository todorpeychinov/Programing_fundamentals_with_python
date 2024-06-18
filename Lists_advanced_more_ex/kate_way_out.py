def find_start_row(map):
    for row in map:
        if 'k' in row:
            return map.index(row)

def find_way_out(map):
    impossible_way = False
    moves = 0
    moves = []
    start_row = find_start_row(map)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ' ':
                moves.append([i, j])
    print(moves)







rows_count = int(input())
map = []

for i in range(rows_count):
    current_row = input()
    map.append(current_row)

result = find_way_out(map)
print(result)



