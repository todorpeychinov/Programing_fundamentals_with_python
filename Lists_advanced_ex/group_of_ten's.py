def group_numbers(list_of_numbers):
    group = 10
    result = []
    while list_of_numbers:
        current_group_numbers = [num for num in list_of_numbers if num <= group]

        list_of_numbers = [num for num in list_of_numbers if num > group]

        result.append(f"Group of {group}'s: {current_group_numbers}")

        group += 10
    return "\n".join(result)

sequence_of_numbers = list(map(int, input().split(', ')))
print(group_numbers(sequence_of_numbers))

