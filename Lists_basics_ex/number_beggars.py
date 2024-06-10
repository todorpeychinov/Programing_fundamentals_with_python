string_of_integers = input().split(", ")
count_of_beggars = int(input())
beggars_sum = []

start_index = 0

for beggar in range(count_of_beggars):
    current_beggar = 0
    for index in range(start_index, len(string_of_integers),count_of_beggars):
        current_beggar += int(string_of_integers[index])
    beggars_sum.append(current_beggar)
    start_index += 1

print(beggars_sum)
