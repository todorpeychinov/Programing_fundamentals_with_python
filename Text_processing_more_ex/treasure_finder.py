def decrypt(message, keys):
    decrypted_message_ = ''
    index = 0
    flag = False

    while not flag:
        for key in keys:
            decrypted_message_ += chr(ord(message[index]) - key)
            index += 1
            if index > len(message) - 1:
                flag = True
                break
    return decrypted_message_


def find_message(message_):
    coordinates = ''
    message_list = message_.split('&')
    treasure_type = message_list[1]

    for index in range(len(message_)):
        if message_[index] == '<':
            index += 1
            while message_[index] != '>':
                coordinates += message_[index]
                index += 1

    return f'Found {treasure_type} at {coordinates}'


key_values = list(map(int, input().split()))

while True:
    encrypted_message = input()

    if encrypted_message == 'find':
        break

    decrypted_message = decrypt(encrypted_message, key_values)
    output_message = find_message(decrypted_message)
    print(output_message)
