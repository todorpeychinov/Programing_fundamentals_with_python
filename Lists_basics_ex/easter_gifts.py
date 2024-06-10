gifts_list = input().split()
command = input()

while command != 'No Money':

    command_list = command.split()
    current_command = command_list[0]
    current_gift = command_list[1]

    if current_command == 'OutOfStock':
        while current_gift in gifts_list:
            gifts_list[gifts_list.index(current_gift)] = 'None'

    elif current_command == 'Required':
        current_index = int(command_list[2])
        if 0 <= current_index < len(gifts_list):
            gifts_list[current_index] = current_gift
    elif current_command == 'JustInCase':
        gifts_list[-1] = current_gift
    command = input()
final_list = []
for gift in gifts_list:
    if gift != 'None':
        final_list.append(gift)

print(" ".join(final_list))
