encrypted_message = input()


while True:
    command = input()

    if command == 'Decode':
        print(f"The decrypted message is: {encrypted_message}")
        break

    command = command.split('|')

    if command[0] == 'Move':
        number_of_letters = int(command[1])
        substring = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters:] + substring

    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]

        left_part = encrypted_message[:index]
        right_part = encrypted_message[index:]
        encrypted_message = left_part + value + right_part

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)



