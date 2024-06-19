energy = int(input())
wins = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break

    else:
        distance = int(command)


    if energy >= distance:
        wins += 1
        energy -= distance

        if wins % 3 == 0:
            energy += wins

    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break


