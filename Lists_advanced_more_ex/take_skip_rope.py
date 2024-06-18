def find_string(take_list, skip_list, current_string):
    result = ''
    index = 0
    start = 0
    while True:
        char_to_take = take_list[index]
        char_to_skip = skip_list[index]
        if char_to_take != 0:
            result += current_string[start:start + char_to_take]
        start += char_to_take + char_to_skip
        index += 1
        if index == len(take_list):
            break


    return result


def process_string(input_string):
    num_list = []
    non_num_list = []

    for character in input_string:
        if character.isdigit():
            num_list.append(int(character))
        else:
            non_num_list.append(character)

    take_list = []
    skip_list = []

    for index in range(len(num_list)):
        if index % 2 == 0:
            take_list.append(num_list[index])
        else:
            skip_list.append(num_list[index])

    result_string = find_string(take_list, skip_list, "".join(non_num_list))
    return result_string


input_string = input()

result_string = process_string(input_string)
print(result_string)
