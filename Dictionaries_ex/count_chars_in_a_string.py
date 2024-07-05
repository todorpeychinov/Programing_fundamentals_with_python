characters = [character for character in input() if character != " "]

my_dictionary = {}

for character in characters:
    if character in my_dictionary:
        my_dictionary[character] += 1
    else:
        my_dictionary[character] = 1

for key, value in my_dictionary.items():
    print(f"{key} -> {value}")

