user_input = input().split()
products_to_search = input().split()
stock = {}

for i in range(0, len(user_input), 2):
    product = user_input[i]
    quantity = int(user_input[i + 1])
    stock[product] = quantity

for current_product in products_to_search:
    if current_product in stock:
        print(f'We have {stock[current_product]} of {current_product} left')
    else:
        print(f'Sorry, we don\'t have {current_product}')

