budget = int(input())

while True:
    user_input = input()
    if user_input == 'End':
        print('You bought everything needed.')
        break
    user_input = int(user_input)
    budget -= user_input
    if budget < 0:
        print("You went in overdraft!")
        break
