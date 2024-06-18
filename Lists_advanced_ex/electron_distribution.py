def calculate_electron_shells(number_of_electrons):
    shield_num = 1
    list_of_shields = []
    while number_of_electrons > 0:
        available_space_in_current_shell = 2 * (shield_num ** 2)
        if available_space_in_current_shell  > number_of_electrons:
            list_of_shields.append(number_of_electrons)
            number_of_electrons = 0
        else:
            list_of_shields.append(available_space_in_current_shell)
            number_of_electrons -= available_space_in_current_shell
        shield_num += 1
    return list_of_shields



num_of_electrons = int(input())
result_list = calculate_electron_shells(num_of_electrons)
print(result_list)