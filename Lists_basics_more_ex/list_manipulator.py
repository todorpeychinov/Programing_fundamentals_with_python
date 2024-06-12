list_of_integers = list(map(int, input().split()))

command = input()

while command != "end":
    command_list = command.split()

    if command_list[0] == 'exchange':
        current_index = int(command_list[1])
        if 0 <= current_index < len(list_of_integers):
            list_of_integers = list_of_integers[current_index + 1:] + list_of_integers[:current_index + 1]
        else:
            print("Invalid index")


    elif command_list[0] == 'max':
        max_index = 'No matches'
        max_number = 0
        if command_list[1] == 'odd':
            index = 0
            for number in list_of_integers:
                if number % 2 != 0:
                    if number > max_number:
                        max_number = number
                        max_index = index
                index += 1
        elif command_list[1] == 'even':
            index = 0
            for number in list_of_integers:
                if number % 2 == 0:
                    if number > max_number:
                        max_number = number
                        max_index = index
                index += 1
        print(max_index)
    elif command_list[0] == 'min':
        min_index = 'No matches'
        min_number = 0
        if command_list[1] == 'odd':
            index = 0
            for number in list_of_integers:
                if number % 2 != 0:
                    if number < min_number:
                        min_number = number
                        min_index = index
                index += 1
        elif command_list[1] == 'even':
            index = 0
            for number in list_of_integers:
                if number % 2 == 0:
                    if number < min_number:
                        min_number = number
                        min_index = index
        print(min_index)
    elif command_list[0] == 'first':
        count = int(command_list[1])
        index = 0
        counter = 0
        list_of_numbers = []
        if count > len(list_of_integers):
            print("Invalid count")
        else:
            if command_list[2] == 'odd':
                for number in list_of_integers:
                    if number % 2 != 0:
                        list_of_numbers.append(number)
                        counter += 1
                    index += 1
                    if counter == count:
                        break
            elif command_list[2] == 'even':
                for number in list_of_integers:
                    if number % 2 == 0:
                        list_of_numbers.append(number)
                        counter += 1
                    if counter == count:
                        break
            print(list_of_numbers)
    elif command_list[0] == 'last':
        count = int(command_list[1])
        counter = 0
        list_of_numbers = []
        if count > len(list_of_integers):
            print("Invalid count")
        else:
            if command_list[2] == 'odd':
                for number in list_of_integers[::-1]:
                    if number % 2 != 0:
                        list_of_numbers.append(number)
                        counter += 1
                    if counter == count:
                        break
            elif command_list[2] == 'even':
                for number in list_of_integers[::-1]:
                    if number % 2 == 0:
                        list_of_numbers.append(number)
                        counter += 1
                    if counter == count:
                        break
            print(list_of_numbers)
    command = input()

print(list_of_integers)