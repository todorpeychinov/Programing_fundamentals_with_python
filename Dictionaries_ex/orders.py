products = {}

while True:
    user_input = input()
    if user_input == 'buy':
        break

    product, price, quantity = user_input.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {'quantity': quantity, 'price': price}
    else:
        products[product]['quantity'] += quantity
        products[product]['price'] = price

for product, product_dict in products.items():
    current_sum = product_dict['price'] * product_dict['quantity']
    print(f'{product} -> {current_sum:.2f}')



