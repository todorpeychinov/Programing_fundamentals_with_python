n = int(input())
stars_count = 1
max_stars = (n * 2) - 1

for i in range(n):
    hollows = (max_stars - stars_count) // 2
    print(hollows * " " + stars_count * "*" + hollows * " ")
    print()
    stars_count += 2


