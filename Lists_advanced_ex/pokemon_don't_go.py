def decrease_and_increase(distances, value):

    for index in range(len(distances)):

        if distances[index] > value:
            distances[index] -= value

        elif distances[index] <= value:
            distances[index] += value




def process_distances(distances):
    gained_points = 0

    while distances:
        index = int(input())

        if index < 0:
            value = distances[0]
            distances[0] = distances[-1]
            decrease_and_increase(distances, value)
            gained_points += value

        elif index > len(distances) - 1:
            value = distances[-1]
            distances[-1] = distances[0]
            decrease_and_increase(distances, value)
            gained_points += value

        else:
            value = distances[index]
            distances.pop(index)
            decrease_and_increase(distances, value)
            gained_points += value

    return gained_points


pokemon_distances = list(map(int, input().split()))

result = process_distances(pokemon_distances)
print(result)