def palindrome_integers(list_of_integers_as_string):
    list_of_bool_results = []
    for number in list_of_integers_as_string:
        if number == number[::-1]:
            list_of_bool_results.append(True)
        else:
            list_of_bool_results.append(False)
    return list_of_bool_results

list_of_integers_as_string = input().split(', ')
result_list = palindrome_integers(list_of_integers_as_string)

for result in result_list:
    print(result)
