user_input = input().split()
stock = {}

for i in range(0, len(user_input), 2):
    product = user_input[i]
    quantity = int(user_input[i + 1])
    stock[product] = quantity

print(stock)
