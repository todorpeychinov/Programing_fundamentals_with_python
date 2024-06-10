from math import floor

group_size = int(input())
days = int(input())

profit = 0
coins_for_food = 2
coins_per_day = 50
coins_for_water = 3
coins_for_boss_slay = 20

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    profit += coins_per_day
    profit -= coins_for_food * group_size
    if day % 3 == 0:
        profit -= coins_for_water * group_size
    if day % 5 == 0:
        profit +=coins_for_boss_slay * group_size
        if day % 3 == 0:
            profit -= 2 * group_size


print(f"{group_size} companions received {floor(profit / group_size)} coins each.")
