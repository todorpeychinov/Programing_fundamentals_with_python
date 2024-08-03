activation_key = input()

while True:
    command = input()

    if command == 'Generate':
        break

    command = command.split('>>>')

    if command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == 'Flip':
        type_of_flip = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring = activation_key[start_index:end_index]
        new_substring = ''

        if type_of_flip == 'Upper':
            new_substring = substring.upper()
        elif type_of_flip == 'Lower':
            new_substring = substring.lower()

        activation_key = activation_key[:start_index] + new_substring + activation_key[end_index:]
        print(activation_key)

    elif command[0] == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")