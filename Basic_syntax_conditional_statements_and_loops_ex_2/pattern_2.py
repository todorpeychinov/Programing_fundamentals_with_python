n = int(input())

print(n * '*')

for i in range(n + 2):
    if i % 2 == 0:
        print()
    else:
        print('*' + (n - 2) * ' ' + '*')

print(n * '*')