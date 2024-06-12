def calculate_order_price(product, quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'water':
        return quantity * 1.0
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'snacks':
        return quantity * 2.0

product = input()
quantity = int(input())

print(f'{calculate_order_price(product, quantity):.2f}')
