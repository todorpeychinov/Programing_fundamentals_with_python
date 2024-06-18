def merge(strings_list, start_index, end_index):
    start_index = max(0, start_index)
    end_index = min(len(strings_list) - 1, end_index)

    if start_index < end_index:
        merged_part = "".join(strings_list[start_index:end_index + 1])
        strings_list[start_index:end_index + 1] = [merged_part]


def divide(strings_list, index, parts):

    if 0 <= index < len(strings_list):
        string_to_divide = strings_list[index]
        part_length = len(string_to_divide) // parts

        divided_parts = []
        start = 0

        for current_part in range(parts):

            if current_part == parts - 1:
                divided_parts.append(string_to_divide[start:])

            else:
                divided_parts.append(string_to_divide[start:start + part_length])
                start += part_length

        strings_list[index:index + 1] = divided_parts


def process_commands(input_strings_list, command_list):

    for command in command_list:
        commands = command.split()
        current_command = commands[0]

        if current_command == 'merge':
            start_index = int(commands[1])
            end_index = int(commands[2])
            merge(input_strings_list, start_index, end_index)

        elif current_command == 'divide':
            index = int(commands[1])
            partitions = int(commands[2])
            divide(input_strings_list, index, partitions)

    return " ".join(input_strings_list)



input_strings_list = input().split()
command_list = []

while True:
    command = input()

    if command == '3:1':
        break

    else:
        command_list.append(command)

result_string = process_commands(input_strings_list, command_list)
print(result_string)