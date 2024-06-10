n = int(input())



for stars in range(1, n + 1, 2):
    hollows = n - stars
    print((hollows // 2) * " " + stars * "*" + (hollows//2) * " ")

for stars in range(n - 2, 0, -2):
    hollows = n - stars
    print((hollows // 2) * " " + stars * "*" + (hollows // 2) * " ")
