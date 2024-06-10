items_list = input().split('|')
bought_items = []
budget = float(input())
profit = 0

for item in items_list:
    item = item.split('->')
    item[1] = float(item[1])
    if item[0] == 'Clothes':
        if item[1] <= 50 and budget >= item[1]:
            budget -= item[1]
            #budget += item[1] * 1.4
            bought_items.append(item[1] * 1.4)
            profit += item[1] * 0.4
    elif item[0] == 'Shoes':
        if item[1] <= 35 and budget >= item[1]:
            budget -= item[1]
            #budget += item[1] * 1.4
            bought_items.append(item[1] * 1.4)
            profit += item[1] * 0.4
    elif item[0] == 'Accessories':
        if item[1] <= 20.50 and budget >= item[1]:
            budget -= item[1]
            #budget += item[1] * 1.4
            bought_items.append(item[1] * 1.4)
            profit += item[1] * 0.4

sum_profit = sum(bought_items)
budget += sum_profit

for item in bought_items:
    current_item = float(item)
    print(f"{current_item:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")