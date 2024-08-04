input_string = input()

while True:
    command = input()

    if command == 'Finish':
        break

    command = command.split()

    if command[0] == 'Replace':
        current_char = command[1]
        new_char = command[2]
        input_string = input_string.replace(current_char, new_char)
        print(input_string)

    elif command[0] == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2]) + 1

        if start_index < 0 or start_index > len(input_string) or end_index < 0 or end_index > len(input_string):
            print("Invalid indices!")

        else:
            input_string = input_string[:start_index] + input_string[end_index:]
            print(input_string)

    elif command[0] == 'Make':
        if command[1] == 'Upper':
            input_string = input_string.upper()
        elif command[1] == 'Lower':
            input_string = input_string.lower()
        print(input_string)

    elif command[0] == 'Check':
        string_to_check = command[1]
        if string_to_check in input_string:
            print(f"Message contains {string_to_check}")
        else:
            print(f"Message doesn't contain {string_to_check}")

    elif command[0] == 'Sum':
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index < 0 or start_index > len(input_string) or end_index < 0 or end_index > len(input_string):
            print("Invalid indices!")

        else:
            substring = input_string[start_index:end_index + 1]
            sum_of_ascii = sum(ord(character) for character in substring)
            print(sum_of_ascii)

