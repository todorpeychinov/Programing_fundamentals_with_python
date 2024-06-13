command = input()
to_do_list = [0] * 10

while command != "End":
    command_list = command.split("-")
    importance = int(command_list[0]) - 1
    note = command_list[1]
    to_do_list.pop(importance)
    to_do_list.insert(importance, note)
    command = input()

print([element for element in to_do_list if element != 0])
