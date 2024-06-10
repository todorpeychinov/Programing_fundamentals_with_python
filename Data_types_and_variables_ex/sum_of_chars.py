number_of_lines = int(input())
char_sum = 0

for i in range(number_of_lines):
    char = input()
    char_sum += ord(char)

print(f"The sum equals: {char_sum}")
