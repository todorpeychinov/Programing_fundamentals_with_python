number_of_rooms = int(input())
flag = False
free_chairs = 0
needed_chairs = 0

for room in range(1, number_of_rooms + 1):
    user_input = input().split()
    chairs_count = len(user_input[0])
    people_count = int(user_input[1])
    if people_count > chairs_count:
        needed_chairs = people_count - chairs_count
        print(f"{needed_chairs} more chairs needed in room {room}")
        flag = True
    else:
        free_chairs += chairs_count - people_count

if not flag:
    print(f"Game On, {free_chairs} free chairs left")

