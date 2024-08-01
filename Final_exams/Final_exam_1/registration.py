def is_valid(username, character):
    if character in username:
        print("Valid username.")
    else:
        print(f"{character} must be contained in your username.")
    return username


def replace(username, character):
    username = username.replace(character, '-')
    print(username)
    return username


def substring_command(username, substring):
    if substring in username:
        username = username.replace(substring, "")
        print(username)
    else:
        print(f"The username {username} doesn't contain {substring}.")

    return username

def reverse_username(username, start_index, end_index):
    substring = username[start_index:end_index]
    substring = substring[::-1]
    print(substring)


def commands_process(commands, username):
    for command in commands:
        split_command = command.split()

        if split_command[0] == 'Letters':
            if split_command[1] == 'Lower':
                username = username.lower()
                print(username)
            elif split_command[1] == 'Upper':
                username = username.upper()
                print(username)


        elif split_command[0] == 'Reverse':
            start_index = int(split_command[1])
            end_index = int(split_command[2]) + 1
            if start_index >= 0 and end_index <= len(username):
                reverse_username(username, start_index, end_index)

        elif split_command[0] == 'Substring':
            substring = split_command[1]
            substring_command(username, substring)

        elif split_command[0] == 'Replace':
            character = split_command[1]
            username = replace(username, character)

        elif split_command[0] == 'IsValid':
            character = split_command[1]
            username = is_valid(username, character)

    return username


current_username = input()
command_list = []

while True:
    current_command = input()
    if current_command == 'Registration':
        break

    command_list.append(current_command)

current_username = commands_process(command_list, current_username)




