def find_substrings_in_strings(substrings, strings):
    result_list = []
    for substring in substrings:
        for string in strings:
            if substring in string:
                result_list.append(substring)
                break
    return result_list

substring_list = input().split(', ')
string_list = input().split(', ')

print(find_substrings_in_strings(substring_list, string_list))

