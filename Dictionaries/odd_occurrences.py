words = input().split()

dictionary = {}

for word in words:
    word = word.lower()

    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1


result_list = []

for key, value in dictionary.items():
    if value % 2 != 0:
        result_list.append(key)

print(" ".join(result_list))
