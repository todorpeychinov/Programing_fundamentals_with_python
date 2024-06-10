line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

winner = 'Draw!'

if line_1[0] == line_1[1] and line_1[1] == line_1[2]:
    if line_1[0] == '1':
        winner = "First"
    elif line_1[0] == '2':
        winner = "Second"

if line_2[0] == line_2[1] and line_2[1] == line_2[2]:
    if line_2[0] == '1':
        winner = "First"
    elif line_2[0] == '2':
        winner = "Second"

if line_3[0] == line_3[1] and line_3[1] == line_3[2]:
    if line_3[0] == '1':
        winner = "First"
    elif line_3[0] == '2':
        winner = "Second"

for i in range(3):
    if line_1[i] == line_2[i] and line_2[i] == line_3[i]:
        if line_1[i] == '1':
            winner = "First"
        elif line_1[i] == '2':
            winner = "Second"

if line_1[0] == line_2[1] and line_2[1] == line_3[2] or \
    line_1[2] == line_2[1] and line_2[1] == line_3[0]:
    if line_2[1] == '1':
            winner = "First"
    elif line_2[1] == '2':
        winner = "Second"

if winner != 'Draw!':
    print(f"{winner} player won")
else:
    print(winner)


