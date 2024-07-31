import re

total_cost = 0
furniture = []
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

user_input = input()

while user_input != 'Purchase':
    match = re.search(pattern, user_input)
    if match:
        current_furniture, cost, quantity = match.groups()
        total_cost += float(cost) * int(quantity)
        furniture.append(current_furniture)

    user_input = input()

print("Bought furniture:")
for current in furniture:
    print(current)
print(f"Total money spend: {total_cost:.2f}")