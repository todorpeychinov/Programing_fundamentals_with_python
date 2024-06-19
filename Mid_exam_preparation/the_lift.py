def find_place_on_the_lift(lift_cabins, waiting_people):
    result = ''

    for current_cabin in lift_cabins:
        available_space = 4 - current_cabin

        if waiting_people > 3:
            waiting_people -= available_space
            lift_cabins[lift_cabins.index(current_cabin)] += available_space

        else:
            if available_space > waiting_people:
                lift_cabins[lift_cabins.index(current_cabin)] += waiting_people
                waiting_people = 0
            else:
                waiting_people -= available_space
                lift_cabins[lift_cabins.index(current_cabin)] = 4


    empty_spots = 4 * len(lift_cabins) - sum(lift_cabins)

    if waiting_people > 0:
        result += f"There isn't enough space! {waiting_people} people in a queue!\n"
    elif empty_spots > 0:
        result += f"The lift has empty spots!\n"

    result += " ".join(map(str, lift_cabins))

    return result


people_in_queue = int(input())
lift_status = list(map(int, input().split()))

result = find_place_on_the_lift(lift_status, people_in_queue)
print(result)