def absolute_value(list_of_values: list) -> list:
    list_of_absolute_values = []
    for value in list_of_values:
        list_of_absolute_values.append(abs(value))
    return list_of_absolute_values


list_of_values = list(map(float, input().split()))
print(absolute_value(list_of_values))


