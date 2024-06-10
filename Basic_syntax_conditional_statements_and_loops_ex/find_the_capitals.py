user_input = input()
list = list()

for index in range(len(user_input)):
    if user_input[index].isupper():
        list.append(index)

print(list)

