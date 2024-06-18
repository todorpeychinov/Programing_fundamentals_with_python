def decipher_message(message):
    list_of_messages = message.split()
    result_list = []
    for message in list_of_messages:
        list_of_nums = [char for char in message if char.isdigit()]
        current_message = [character for character in message if not character.isdigit()]
        current_message.insert(0,chr(int("".join(list_of_nums))))
        help_char = current_message[1]
        current_message[1] = current_message[-1]
        current_message[-1] = help_char
        result_list.append("".join(current_message))
    return " ".join(result_list)

message = input()
print(decipher_message(message))

