n = int(input())

dictionary = {}


for i in range(n):
    word = input()
    synonym = input()

    if word in dictionary:
        dictionary[word].append(synonym)
    else:
        dictionary[word] = [synonym]

for key, value in dictionary.items():
    print(f'{key} - {", ".join(value)}')