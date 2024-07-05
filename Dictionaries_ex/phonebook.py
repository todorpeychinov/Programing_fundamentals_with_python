phonebook = {}

while True:
    user_input = input()

    if '-' not in user_input:
        searches = int(user_input)
        break

    name, number = user_input.split('-')
    phonebook[name] = number

for search in range(searches):
    current_name = input()
    if current_name in phonebook:
        print(f'{current_name} -> {phonebook[current_name]}')
    else:
        print(f'Contact {current_name} does not exist.')
