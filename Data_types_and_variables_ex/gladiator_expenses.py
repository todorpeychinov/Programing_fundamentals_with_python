lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
counter = 0

expenses = 0

for i in range(1, lost_fight_count + 1):
    if i % 2 == 0:
        expenses += helmet_price
    if i % 3 == 0:
        expenses += sword_price
    if i % 2 == 0 and i % 3 == 0:
        expenses += shield_price
        counter += 1
        if counter % 2 == 0:
            expenses += armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')