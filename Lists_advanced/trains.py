wagons_count = int(input())
wagon_list = [0] * wagons_count

command = input()

while command != 'End':
    command_list = command.split()
    if command_list[0] == 'add':
        people_count = int(command_list[1])
        wagon_list[-1] += people_count
    elif command_list[0] == 'insert':
        index = int(command_list[1])
        people_count = int(command_list[2])
        wagon_list[index] += people_count
    elif command_list[0] == 'leave':
        index = int(command_list[1])
        people_count = int(command_list[2])
        wagon_list[index] -= people_count
    command = input()

print(wagon_list)

