number_of_lines = int(input())

for line in range(number_of_lines):
    some_string = input()
    name = ''
    age = ''

    for index in range(len(some_string)):
        if some_string[index] == '@':
            index += 1
            while some_string[index] != '|':
                name += some_string[index]
                index += 1

        if some_string[index] == '#':
            index += 1
            while some_string[index] != '*':
                age += some_string[index]
                index += 1


    print(f"{name} is {age} years old.")
