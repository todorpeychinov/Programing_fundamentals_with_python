list = list()
user_input = input()

list = user_input.split(", ")
counter = len(list)
for index in range(0, len(list)):
    if list[index] == 'wolf':
        if index == (len(list) - 1):
            print('Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {counter - index - 1}! You are about to be eaten by a wolf!')
