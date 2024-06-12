def chars_in_range(start_char, end_char):
    result_string = ''
    for char in range(ord(start_char) + 1, ord(end_char)):
        result_string += chr(char) + ' '
    return result_string


start_char = input()
end_char = input()

print(chars_in_range(start_char, end_char))