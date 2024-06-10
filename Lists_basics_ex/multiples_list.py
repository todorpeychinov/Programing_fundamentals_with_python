factor = int(input())
count = int(input())
integer_list = []

for number in range(factor, (count * factor) + 1, factor):
    integer_list.append(number)

print(integer_list)

