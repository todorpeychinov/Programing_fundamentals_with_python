number = input()
max_number = ''
my_list = list()


for index in range(len(number)):
    number = int(number)
    my_list.append(number % 10)
    number //= 10

my_list.sort()

for digit in range(len(my_list) - 1, -1, -1):
    max_number += str(my_list[digit])

print(int(max_number))







