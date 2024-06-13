def sort_names(list_of_names):
    sorted_names = sorted(list_of_names, key=lambda name: (-len(name), name))
    return sorted_names

names = input().split(', ')
print(sort_names(names))


