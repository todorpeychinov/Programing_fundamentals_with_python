import re

pattern = r'%([A-Z][a-z]+)%([^$|%.]*)<(\w+)>([^$|%.]*)\|([0-9]+)\|([^$|%.]*)(([0-9]*(\.*[0-9]+)?\$))'
pattern_2 = r'([0-9]+\.*[0-9]+)\$'
income = 0

while True:
    current_input = input()

    if current_input == 'end of shift':
        break

    matches = re.match(pattern, current_input)

    if matches:
        name = matches.group(1)
        product = matches.group(3)
        quantity = int(matches.group(5))
        matches_as_str = matches.group()
        matches_list = matches_as_str.split('|')
        price_as_str = matches_list[2]
        price_match = re.findall(pattern_2, price_as_str)
        price = float(*price_match)

        total_price = price * quantity
        income += total_price
        print(f'{name}: {product} - {total_price:.2f}')

print(f'Total income: {income:.2f}')